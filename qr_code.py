# Podemos utilizar o qr code para identificação de equipamentos eletrônicos
# https://www.thepythoncode.com/article/generate-read-qr-code-python   -    https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/   -   https://www.guj.com.br/t/resolvido-ler-qr-code-usando-python/383136/2

# Importing library
import qrcode
 
# Data to be encoded
data = 'QR Code using make() function'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode1.png')



# -------------------------------------------------

# Importing library
import qrcode
 
# Data to encode
data = "GeeksforGeeks"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
 
img.save('MyQRCode2.png')
