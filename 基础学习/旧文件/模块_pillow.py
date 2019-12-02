from PIL import Image

#打开一个jpg图像文件，注意这是当前路径
im = Image.open('C:\美食.jps')
#获得图片尺寸
w,h = im.size
print('Original image size:%sx%s'%(w,h))
#缩放到50%
im.thumbnail((w//2,h//2))
print('Resize image to:%sx%s'%(w//2,h//2))
#用jpeg保存图片
im.seve('thumbnail.jpg','jpeg')
