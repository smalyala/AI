from random import *

population = []
for x in range(12):
	temp = []
	for y in range(10):
		temp.append(randint(0,1))
	population.append(temp)
