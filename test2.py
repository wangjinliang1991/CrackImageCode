import pytesseract
from PIL import Image

# 对于code3.jpg，验证码内的多余线条干扰图片的识别
# 转灰度图像
image = Image.open("code.jpg")
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()
result = pytesseract.image_to_string(image)
print(image)


# result = pytesseract.image_to_string(image)
# print(result)

