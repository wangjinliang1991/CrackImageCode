# import pytesseract
# from PIL import Image
#
# # 正常验证码
# image = Image.open("code4.png")
# result = pytesseract.image_to_string(image, lang='chi-sim')
# print(result)
#
# 最开始没搞定变量的笨方法
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'D:/pythonic/tesseract/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "D:/pythonic/tesseract/Tesseract-OCR/tessdata"'

image = Image.open("code4.png")
code = pytesseract.image_to_string(image, config=tessdata_dir_config, lang='chi-sim')
print(code)