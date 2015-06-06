from random import random, choice
from time import clock
TRIALS = 9000
ALPHA = .25
INPUTS = [(0, 0, -1, 0), (0, 1, -1, 1), (1, 0, -1, 1), (1, 1, -1, 0)]
SMALL = .4

# def trainPerceptronsWeights():
# 	epochs = 0

# 	w = [random()*2-1]*(len(INPUTS) + 1)
# 	while epochs < TRIALS and not trained(w):
# 		for x in INPUTS:
# 			x = choice(INPUTS)
# 			t = x[3]
# 			y = f(w, x)
# 			w[0] = w[0] - ALPHA*(y-t)*x[0]
# 			w[1] = w[1] - ALPHA*(y-t)*x[1]
# 			w[2] = w[2] - ALPHA*(y-t)*x[2]
# 		epochs += 1
# 	return w, epochs

# def f(w, x):
# 	return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2]) > 0)

def yValue(x, w, v):
	h = [0, 0, -1]
	h[0] = int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
	h[1] = int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
	y = int((v[0]*h[0] + v[1]*h[1] + v[2]*h[2]) > 0)
	return y

def trained(w, v):
	for x in INPUTS:
		y = yValue(x, w, v)
		t = x[3]
		if y != t:
			return False
	return True

def verifyNetwork(epochs, w, v):
	print('Epochs =', epochs)
	for x in INPUTS:
		t = x[3]
		y = yValue(x,w,v)
		print('%5s'% (y == t), '--->', yValue(x,w,v), x)
	print('\n=== Statistics ===')
	print(' x = %2d, %2d, %2d, %2d'%(x[0], x[1], x[2], x[3]))
	print(' w = %5.2f, %5.2f'%(w[0][0], w[0][1]))
	print('     %5.2f, %5.2f'%(w[1][0], w[1][1]))
	print('     %5.2f, %5.2f'%(w[2][0], w[2][1]))
	print(' v = %5.2f, %5.2f, %5.2f'%(v[0], v[1], v[2]))
	print(' y =', y)
	
def initializeWeights():
	w = [[-1, 1,], [-1, 1,], [-1.5, .5,],]
	v = [1, 1, 1.5]
	return w, v

def improveWeights(w, v):
	w = [[random()*2-1]*2, [random()*2-1]*2]
	return w, v

def trainNetwork():
	epochs = 0
	h = [0, 0, -1]
	w, v = initializeWeights()
	while epochs < TRIALS and not trained(w, v):
		x = choice(INPUTS)
		w, v = improveWeights(w, v)
		h[0] = int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
		h[1] = int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
		epochs += 1
	return epochs, w, v

def main():
	epochs, w, v = trainNetwork()
	verifyNetwork(epochs, w, v)

if __name__ == '__main__': START_TIME = clock(); main(); \
						   print('--> Run time =', round(clock() - START_TIME, 2), 'seconds <--');