from tkinter import *
from time import clock
from random import randint
from math import *

root = Tk()
START = clock()
WIDTH = 512
HEIGHT = 512
COLORFLAG = False
HIGH = 45
LOW = 10
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 6


class ImageFrame:
	def __init__(self, image, COLORFLAG = False):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT):
			for col in range(WIDTH):
				num = image[row*WIDTH + col]
				if COLORFLAG == True:
					kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
				else:
					kolor = '#%02x%02x%02x' % (num, num, num)
				self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)

def displayImageWindow(image):
	global x
	x = ImageFrame(image)

def imageNoise(points, image):
	for n in range(points):
		r = randint(0, HEIGHT-1);
		c = randint(0, WIDTH-1);
		image[WIDTH*r+c] = 255;

def drawLineMB(m, b, image):
	for x in range(WIDTH):
		index = WIDTH * int(m*x+b) + x;
		if 0 <= index < len(image):
			image[index] = 255;

def drawLineRT(r, T, image):
	x = r * cos(T);
	y = r * sin(T);
	m = -x/y;
	b = x*x/y + y;
	drawLineMB(m, b, image);

def drawCircle(r, image):
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if (pow((x-256), 2) + pow((y-256), 2)) <= pow(r, 2):
				index = WIDTH * y + x;
				image[index] = 255;

def main():
	image = [0] * HEIGHT * WIDTH
	#imageNoise(500, image);
	#drawLine(0, 100, image);
	#drawLineMB(1, 0, image);
	drawLineRT(300, pi/3, image);
	#drawCircle(50, image)
	displayImageWindow(image);
	root.mainloop()
main();