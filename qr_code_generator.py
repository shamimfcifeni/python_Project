import qrcode

def create_qr_code(data, filename):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code (URL, text, etc.): ")
    filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
    create_qr_code(data, filename)