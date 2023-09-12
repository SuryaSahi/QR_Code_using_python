import qrcode as qr
img = qr.make("https://youtu.be/2LsOyOaobrc?si=Z4VDI-J-Tfmn64cK")
img.save("request.png")

