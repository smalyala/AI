from math import *
from random import *

RADIUS = .001

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def f(x, y):
	if x <= 0 or x >= 10 or y <= 0 or y >= 10:
		return float('inf')
	return (x*sin(4*x) + 1.1*y*sin(2*y))

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
