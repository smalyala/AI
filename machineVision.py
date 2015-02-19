from tkinter import *
from time import clock

root = Tk()
START = clock()
WIDTH = 512
HEIGHT = 512
COLORFLAG = False
HIGH = 45
LOW = 10
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 6

def main():
	global WIDTH,HEIGHT
	file1 = open('stubs.ppm', 'r')
	stng = file1.readline()
	print(stng)
	nums = file1.read().split()
	print(nums[:10])
	file1.close()

	WIDTH = int(nums[0])
	HEIGHT = int(nums[1])

	image = [];
	for pos in range(3, len(nums), 3):
		RGB = (int(nums[pos+0]), int(nums[pos+1]), int(nums[pos+2]))
		image.append(int(.2*RGB[0] + .7*RGB[1] + .1*RGB[2]))
	printElapsedTime('Gray numbers are now created.')

	file1 = open('grayScale.ppm', 'w')
	for elt in image:
		file1.write(str(elt) + " ")
	printElapsedTime('saved file numbers')
	file1.close()

	displayImageWindow(image)

	root.mainloop()

def printElapsedTime(msg = 'time'):
	length = 30
	msg = msg[:length]
	tab = '.'*(length-len(msg))
	print('--' + msg.upper() + tab + ' ', end = '')
	time = round(clock() - START, 1)
	print('%2d'%int(time/60), ' min:', '%4.1f'%round(time%60, 1), ' sec', sep = '')

def displayImageWindow(image):
	global x
	x = ImageFrame(image)

class ImageFrame:
	def __init__(self, image, COLORFLAG = False):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT):
			for col in range(WIDTH):
				#print(row*WIDTH + col, WIDTH, row, col, len(image));
				if (row*WIDTH + col) < len(image):
					num = image[row*WIDTH + col]
					if COLORFLAG == True:
						kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
					else:
						kolor = '#%02x%02x%02x' % (num, num, num)
					self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)
		printElapsedTime('displayed image')
main();
