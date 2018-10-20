from PIL import Image, ImageFilter
#读取图像
im = Image.open( 'code.jpg' )
#显示图像
im.show()

#过滤图像
im_sharp = im.filter( ImageFilter.SHARPEN )
#保存过滤过的图像到文件中
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#分解图像到三个RGB不同的通道（band）中。
r,g,b = im_sharp.split()

#显示被插入到图像中的EXIF标记
exif_data = im._getexif()
exif_data