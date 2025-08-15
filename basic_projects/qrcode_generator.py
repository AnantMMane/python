import qrcode

data = input('Please enter your URL: ').strip()
file_name = input('Please enter your file name: ').strip()

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(data)
image = qr.make_image(file_name=file_name)
image.save(file_name)
print('QR Code has been saved in', file_name)

#input 1: www.google.com
#input 2: google_qr.png

