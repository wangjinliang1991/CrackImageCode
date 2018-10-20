import pytesseract
from PIL import Image, ImageFilter

im = Image.open("code.jpg")
im_sharp = im.filter( ImageFilter.SHARPEN )
# im_sharp.save( 'image_sharpened.jpg', 'JPEG' )
result = pytesseract.image_to_string(im_sharp)
print(result)