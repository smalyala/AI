def randomlyAssignWeights():
	w = [[uniform(-1, 1),uniform(-1, 1),uniform(-1, 1),] for row in range(9)]
	v = [[uniform(-1, 1),uniform(-1, 1),uniform(-1, 1),uniform(-1, 1), uniform(-1, 1),
		uniform(-1, 1), uniform(-1, 1),uniform(-1, 1),] for row in range(4)]
	return w, v

def mult(v,m):
	assert len(v) == len(m), [len(v), len(m)]
	return [sum([v[i]*m[i][j]
				for i in range(len(v))])
					for j in range(len(m[0]))]

def printAllData(w, h, v, y):
	pass

def f(x):
	return 1/(1+exp(-x))

def feedForward(x,w,v):
	dp = []
	h = []
	DP = []
	y = []
	dp.append(w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2] + w[3][0]*x[3] + \
			w[4][0]*x[4] + w[5][0]*x[5] + w[6][0]*x[6] + w[7][0]*x[7] + w[8][0]*x[8])
	dp.append(w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2] + w[3][1]*x[3] + \
			w[4][1]*x[4] + w[5][1]*x[5] + w[6][1]*x[6] + w[7][1]*x[7] + w[8][1]*x[8])
	dp.append(w[0][2]*x[0] + w[1][2]*x[1] + w[2][2]*x[2] + w[3][2]*x[3] + \
			w[4][2]*x[4] + w[5][2]*x[5] + w[6][2]*x[6] + w[7][2]*x[7] + w[8][2]*x[8])
	h.append(f(dp[0]))
	h.append(f(dp[1]))
	h.append(f(dp[2]))
	h.append(-1)
	DP.append(v[0][0]*h[0] + v[1][0]*h[1] + v[2][0]*h[2] + v[3][0]*h[3])
	DP.append(v[0][1]*h[0] + v[1][1]*h[1] + v[2][1]*h[2] + v[3][1]*h[3])
	DP.append(v[0][2]*h[0] + v[1][2]*h[1] + v[2][2]*h[2] + v[3][2]*h[3])
	DP.append(v[0][3]*h[0] + v[1][3]*h[1] + v[2][3]*h[2] + v[3][3]*h[3])
	DP.append(v[0][4]*h[0] + v[1][4]*h[1] + v[2][4]*h[2] + v[3][4]*h[3])
	DP.append(v[0][5]*h[0] + v[1][5]*h[1] + v[2][5]*h[2] + v[3][5]*h[3])
	DP.append(v[0][6]*h[0] + v[1][6]*h[1] + v[2][6]*h[2] + v[3][6]*h[3])
	DP.append(v[0][7]*h[0] + v[1][7]*h[1] + v[2][7]*h[2] + v[3][7]*h[3])
	y.append(f(DP[0]))
	y.append(f(DP[1]))
	y.append(f(DP[2]))
	y.append(f(DP[3]))
	y.append(f(DP[4]))
	y.append(f(DP[5]))
	y.append(f(DP[6]))
	y.append(f(DP[7]))
	t = x
	E = .5*(y[0]-t[0])**2 + .5*(y[1]-t[1])**2 + .5*(y[2]-t[2])**2 + .5*(y[3]-t[3])**2 + \
		.5*(y[4]-t[4])**2 + .5*(y[5]-t[5])**2 + .5*(y[6]-t[6])**2 + .5*(y[7]-t[7])**2
	print(E)
	return dp, h, DP, y

def backPropagation(x,w,dp,h,v,DP,y,):
	return w,v

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

def trainNetwork():
	epochs = 0
	w, v = randomlyAssignWeights();
	while epochs < TRIALS:
		for x in INPUTS:
			dp, h, DP, y = feedForward(x,w,v)
			w, v = backPropagation(x,w,dp,h,v,DP,y,)
		epochs += 1
		print('epochs =', epochs)
	return epochs, w, v

from random import *
from math import *
from time import *
TRIALS = 9000
ALPHA = .25
INPUTS = [[1, 0, 0, 0, 0, 0, 0, 0, -1]]

def main():
	epochs,w,v = trainNetwork()
	#verifyNetwork(epochs,w,v)

if __name__ == '__main__': START_TIME = clock(); main(); \
						   print('--> Run time =', round(clock() - START_TIME, 2), 'seconds <--');