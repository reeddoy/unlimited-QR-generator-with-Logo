import qrcode
from PIL import Image, ImageDraw
import os

# Directory to save the QR code images
os.makedirs('qr_codes', exist_ok=True)

# Path to the logo image
# logo_path = 'logo.png'
logo_path = 'logo.jpg'

# Create 100 QR codes with a logo in the center
for i in range(1, 101):
    # Data to encode in the QR code
    data = f"Hi. This is developer Arif. Thanks for visiting. {i}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Use high error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white').convert('RGB')
    
    # Load the logo image
    logo = Image.open(logo_path)
    
    # Calculate the size of the logo
    qr_width, qr_height = img.size
    logo_size = qr_width // 5  # Scale logo size to be 1/5th of the QR code size
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    
    # Calculate the position to paste the logo
    logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    
    # Create a white circle on the QR code where the logo will be placed
    draw = ImageDraw.Draw(img)
    circle_center = (qr_width // 2, qr_height // 2)
    circle_radius = logo_size // 2
    draw.ellipse(
        [
            (circle_center[0] - circle_radius, circle_center[1] - circle_radius),
            (circle_center[0] + circle_radius, circle_center[1] + circle_radius)
        ],
        fill='white'
    )
    
    # Paste the logo onto the QR code
    img.paste(logo, logo_pos)
    
    # Save the QR code with logo
    img.save(f'qr_codes/qr_code_{i}.png')
