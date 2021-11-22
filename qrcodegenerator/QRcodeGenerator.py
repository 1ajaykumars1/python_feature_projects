# qr code generator
# first you need to install 2 modules
# qr code (pip install qrcode)
# image (pip install image)
# in cmd

import qrcode
import image
qr = qrcode.QRCode(
    version=5,  # 15 means the version of the qr code high the number bigger the code image and complicated pictures
    box_size=5,    # size of the box where qr code will be displayed
    border=5,       # it is the white part of image -- border in all 4 slides with white color
)
data = "https://www.youtube.com/playlist?list=PLBwF487qi8MGU81nDGaeNE1EnNEPYWKY_"
# as i have given the path of my channel like the same way you can give anything
# if you dont want to redirect and create for normal text that write text in the quotes

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("text.png")
