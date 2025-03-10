from random import *
from math import *

MAX = 20
POP = 200

def cost(x, y):
	return x*sin(4*x) + 1.1*y*sin(2*y)

def createPopulation():
	m = [''.join([str(randint(0,1)) for c in range(MAX)]) for r in range(POP)]
	return m

def printMatrix(matrix):
	for row in matrix:
		for col in row:
			print(col, end = '  ')
		print('')
	print('####################################')

def allSame(matrix):
	curr = matrix[0]
	for row in matrix:
		if curr != row:
			return False
	return True

def main():
	population = createPopulation();
	sameYet = False
	z = 0
	for s in range(POP):
		H = len(population[s])//2
		x = int(population[s][0:H], 2)
		y = int(population[s][H:], 2)
		population[s] = (cost(x, y), population[s])
	while sameYet == False:
		newPop = []
		for s in range(POP):
			H = len(population[s][1])//2
			x = int(population[s][1][0:H], 2)
			y = int(population[s][1][H:], 2)
			population[s] = (cost(x, y), population[s][1])
		population.sort()
		population.reverse()
		for s in range(1, (len(population)//2)+1):
			parent1 = population[0]
			parent2 = population[s]
			r = randint(1,19)
			child1 = parent1[0:r] + parent2[r:]
			child2 = parent2[0:r] + parent1[r:]
			newPop.append(child1)
			newPop.append(child2)
		population = newPop
		z += 1
		sameYet = allSame(population)
	print('	 Generation ' + repr(z))
	printMatrix(population)
main()
