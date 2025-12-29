"""
QR Code Generator
Author: Satria Dwi Cahya
Purpose: Understanding library and function works 
"""
import qrcode
import os
os.system('cls')
qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 10,
        border = 4,
    )

def QRCode(link, file_name):
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    type(img)  
    img.save(f"{file_name}.png")
    print(f'QR code saved as {file_name}.png')

def CostumQRCode(link, file_name):
    fill_clr = input('Fill Color: ')
    background_clr = input('Backgroud Color: ')

    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color = fill_clr, back_color = background_clr)
    type(img)  
    img.save(f"{file_name}.png")
    print(f'QR code saved as {file_name}.png')


print('QR Code Generator')
print('-----------------')
user_selec = int(input('How many QR codes do you want to create? (Number): '))

for x in range(user_selec):
    link = input('Enter the text or URL for the  QR code: ')
    file_name = input('Enter the file name: ')
    add_color = input('Add color of QR Codes? (Y/N): ').lower()


    if add_color == 'y':
        CostumQRCode(link, file_name)
    else:
        QRCode(link, file_name)



