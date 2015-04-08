from random import *

def findFittest(matrix):
	ind = 0
	i = 0
	fittest = 0
	for parent in matrix:
		fit = sum(parent)
		if fittest < fit:
			ind = i
			fittest = fit
		i += 1
	return ind

def printMatrix(matrix):
	for row in matrix:
		for col in row:
			print(col, end = '  ')
		print('')
	print('####################################')

def allSame(matrix):
	curr = sum(matrix[0])
	for row in matrix:
		val = sum(row)
		if curr != val:
			return False
	return True


population = []
for x in range(12):
	temp = []
	for y in range(10):
		temp.append(randint(0,1))
	population.append(temp)
sameYet = False
times = 0
while sameYet == False and times < 25:
	newPop = []
	pos = findFittest(population)
	temp = population[0]
	population[0] = population[pos]
	population[pos] = temp
	for x in range(1, len(population)):
		parent1 = population[0]
		parent2 = population[x]
		r = randint(1,9)
		child1 = parent1[0:r] + parent2[r:]
		child2 = parent2[0:r] + parent1[r:]
		newPop.append(child1)
		newPop.append(child2)
	population = newPop
	#printMatrix(population)
	sameYet = allSame(population)
	times += 1
	print(sameYet, sameYet)
printMatrix(population)