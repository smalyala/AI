def setUpCanvas(root):
	root.title("Fractal flowers by Sahith.")
	canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def displayStatistics():
	print('RUN TIME = %6.2f' % round(clock()-START_TIME, 2), 'seconds.')
	root.title('The fractal flower is complete.')

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def line(x1, y1, x2, y2, kolor = 'WHITE', width = 1):
	canvas.create_line(x1, y1, x2, y2, width = width, fill = kolor)

def drawFlower(cx, cy, radius):
	if radius < 3:
		return
	kolor = 'GREEN'
	width = 2
	if radius < 50:
		kolor = 'WHITE'
		width = 1
	if radius < 10:
		kolor = 'RED'
		width = 1
	for t in frange(0, 6.28, .9):
		x = cx + radius*sin(t)
		y = cy + radius*cos(t)
		for z in range(7):
			line(cx, cy, x, y, kolor, width)
			tx = x
			ty = y
		drawFlower(x, y, radius/3);
	canvas.update()

from tkinter import *
from math import *
from random import *
from time import *
root = Tk()
canvas = setUpCanvas(root)
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
START_TIME = clock()

def main():
	drawFlower(WIDTH/2, HEIGHT/2 - 50, 240)
	displayStatistics()
	root.mainloop()

if __name__ == '__main__': main()
