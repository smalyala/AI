from math import *
from random import *
from time import *

RADIUS = .001
AREA = 100

def generator():
	side = int(sqrt(AREA))
	for x in range(side):
		for y in range(side):
			yield(x,y)

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def f(x, y):
	if x <= 0 or x >= 10 or y <= 0 or y >= 10:
		return float('inf')
	return (x*sin(4*x) + 1.1*y*sin(2*y))

def addVectors(p1, p2):
	x1 = p1[1]
	y1 = p1[2]
	x2 = p2[1]
	y2 = p2[2]
	x = x1 + x2
	y = y1 + y2
	return((f(x,y), x, y))

def mulVector(p, scal):
	x = p[1] * scal
	y = p[2] * scal
	return((f(x,y), x, y))

def subVectors(p1, p2):
	x1 = p1[1]
	y1 = p1[2]
	x2 = p2[1]
	y2 = p2[2]
	x = x1 - x2
	y = y1 - y2
	return((f(x,y), x, y))

def midpoint(p1, p2):
	x1 = p1[1]
	y1 = p1[2]
	x2 = p2[1]
	y2 = p2[2]
	x = (x1 + x2)/2
	y = (y1 + y2)/2
	return((f(x,y), x, y))

def part1():
	start = clock()
	print('Part 1')
	x = random() * 10
	y = random() * 10
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for a in range(100):
		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + RADIUS*cos(t)
			trialY = y + RADIUS*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
		x = bestX
		y = bestY
	print(bestX, bestY, bestF)
	end = clock()
	tim = -1 * (start - end)
	print('Time taken', round(tim, 3))
	print('')

def part2():
	start = clock()
	print('Part 2')
	x = random() * 10
	y = random() * 10
	bestX = float('inf')
	bestY = float('inf')
	cosD = dict()
	sinD = dict()
	bestF = float('inf')
	for a in range(100):
		for t in frange(0, 2*pi, 2*pi/64):
			if t in cosD.keys():
				trialX = x + RADIUS*cosD[t]
			else:
				val = cos(t)
				trialX = x + RADIUS*val
				cosD[t] = val
			if t in sinD.keys():
				trialY = y + RADIUS*sinD[t]
			else:
				val = sin(t)
				trialY = y + RADIUS*val
				sinD[t] = val
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
		x = bestX
		y = bestY
	print(bestX, bestY, bestF)
	end = clock()
	tim = -1 * (start - end)
	print('Time taken', round(tim, 3))
	print('')

def part3():
	start = clock()
	print('Part 3')
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for coord in generator():
		x = coord[0]
		y = coord[1]
		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + RADIUS*cos(t)
			trialY = y + RADIUS*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
		x = bestX
		y = bestY
	print(bestX, bestY, bestF)
	end = clock()
	tim = -1 * (start - end)
	print('Time taken', round(tim, 3))
	print('')

def part4():
	start = clock()
	print('Part 4')
	x = random() * 10
	y = random() * 10
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for a in range(10000):
		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + RADIUS*cos(t)
			trialY = y + RADIUS*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
		x = bestX
		y = bestY
	print(bestX, bestY, bestF)
	end = clock()
	tim = -1 * (start - end)
	print('Time taken', round(tim, 3))
	print('')

def part5():
	tempList = [(random()*10, random()*10) for x in range(3)]
	tempTup = []
	for s in range(3):
		x = tempList[s][0]
		y = tempList[s][1]
		tempTup.append((f(x,y), x, y))
	tempTup.sort()
	a = tempTup[2]
	b = tempTup[0]
	c = tempTup[1]
	m = midpoint(b, c)
	d = subVectors(addVectors(b,c), a)
	e = subVectors(addVectors(mulVector(b, 1.5), mulVector(c, 1.5)), mulVector(a, 2))
	f = subVectors(addVectors(mulVector(b, .75), mulVector(c, .75)), mulVector(a, .5))
	g = addVectors(addVectors(mulVector(b, .25), mulVector(c, .25)), mulVector(a, .5))
	

part1()
part2()
part3()
part4()
