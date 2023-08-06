
from PIL import Image,ImageEnhance,ImageFilter

def process(im):
	data = im.getdata()
	w,h = im.size
	black_point = 0
	for x in range(1,w-1):
		for y in range(1,h-1):
			mid_pixel = data[w*y+x] #中央像素点像素值
			if mid_pixel < 200: #找出上下左右四个方向像素点像素值
				top_pixel = data[w*(y-1)+x]
				left_pixel = data[w*y+(x-1)]
				down_pixel = data[w*(y+1)+x]
				right_pixel = data[w*y+(x+1)]

				#判断上下左右的黑色像素点总个数
				if top_pixel < 100:
					black_point += 1
				if left_pixel < 100:
					black_point += 1
				if down_pixel < 100:
					black_point += 1
				if right_pixel < 100:
					black_point += 1
				if black_point >= 2:
					im.putpixel((x,y),0)
				else:
					im.putpixel((x,y),255)
				#print black_point
				black_point = 0
	return im



def img_clear(im):
	enhancer = ImageEnhance.Contrast(im)
	im = enhancer.enhance(2)
	im = im.convert('L')
	for i in range(5):
		im = process(im)
	return im

if __name__ == "__main__":
	img_name = '123.png'
	#去除干扰线
	im = Image.open(img_name)
	im = img_clear(im)
	im.save("4.png","png")

