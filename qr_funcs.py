from datetime import datetime, timedelta
import qrcode
import random
cnt=130
def generate_dynamic_qr_code_img(uuid = "37b900f0-25c0-448b-825a-74d62c8ceb41"):
    # Generate timestamp 10 seconds in the future
    global cnt
    now = datetime.utcnow() 
    second = now.second//15*15
    current_time = now.strftime(f"%Y-%m-%d_%H:%M:{second:02}.{cnt:03}") + ".UTC"
    cnt+=1
    if cnt>320:
        cnt=100
    # Combine the UUID and timestamp
    qr_data = f"{uuid}_{current_time}"

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code, version 1 is 21x21
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    print(qr_data)
    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def generate_bag_qr_code_img(bag_id):
    # bag_id = bag_id
    # Create QR Code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code, version 1 is 21x21
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size
    )
    qr.add_data(bag_id.upper())
    qr.make(fit=True)
    # print(qr_data)
    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    return img
