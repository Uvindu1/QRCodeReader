import qrcode
import image
qr = qrcode.QRCode(
    version= 10,# kochchara sankeerana wenna onada kiyana eka wage
    box_size= 10, # disply karanna ona qr eke size eka
    border= 5 # wateta enna ona sudupata boder eka
)

data = "https://www.youtube.com/watch?v=BdpON_IKGNc" #qr code eka athulata dana deya

qr.add_data(data)#qr code eka athulata demima
qr.make(fit=True)
img = qr.make_image(fill="black", back_color= "white")
img.save("test.png")












