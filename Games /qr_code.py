import qrcode

urls = input('Enter URLs separated by commas: ').split(',')

for i, url in enumerate(urls, 1):
    url = url.strip()
    fill_color = input(f'Enter fill color for QR {i}: ').strip()
    back_color = input(f'Enter background color for QR {i}: ').strip()
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    
    image = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )
    
    filename = f'qr_{i}.png'
    image.save(filename)
    print(f'QR code saved as {filename}')