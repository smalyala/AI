#################################################
#Name: Sahith Malyala  Date: 11/20/14   Period: 1
#################################################


from copy import deepcopy

def quad(lst, r, c):
	if r < 3:
		boundR = 3;
	elif r < 6:
		boundR = 6;
	elif r < 9:
		boundR = 9;
	if c < 3:
		boundC = 3;
	elif c < 6:
		boundC = 6;
	elif c < 9:
		boundC = 9;
	r = boundR - 3;
	c = boundC - 3;
	while r < boundR:
		c = boundC-3;
		while c < boundC:
			ch = matrix[r][c];
			if ch != '.' and ch not in lst:
				lst.append(ch);
			c += 1;
		r += 1;
	return lst;


def isSolved(matrix):
	allPos = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
	for r in matrix:
		for val in allPos:
			if val not in r:
				return False;
	for i in range(9):
		col = [];
		down = 0;
		while down < 9:
			col.append(matrix[i][down])
			down += 1;
		for val in allPos:
			if val not in col:
				return False;
	boundR = 3;
	boundC = 3;
	rmin = 0;
	cmin = 0;
	count = 1;
	for t in range(9):
		occ = [];
		r = rmin;
		while r < boundR:
			c = cmin;
			while c < boundC:
				occ.append(matrix[r][c]);
				c += 1;
			r += 1;
		for val in allPos:
			if val not in occ:
				return False;
		boundC += 3;
		cmin += 3;
		if count == 6:
			rmin = 6;
			cmin = 0;
			boundR = 9;
			boundC = 3;
		elif count == 3:
			rmin = 3;
			cmin = 0;
			boundR = 6;
			boundC = 3;
		count += 1;
	return True;		

def findNbrs(matrix): #returns the neighbor dictionary for the location tuple (r,c)
	nbrs = {};
	locs = [];
	r = 0;
	while r < 9:
		c = 0;
		while c < 9:
			if matrix[r][c] == '.':
				lst = [];
				for ch in matrix[r]:
					if ch != '.' and ch not in lst:
						lst.append(ch);
				down = 0;
				while down < 9:
					ch = matrix[down][c];
					if ch != '.' and ch not in lst:
						lst.append(ch);
					down += 1;
				lst = quad(lst, r, c);
				nbrs[(r, c)] = lst;
				locs.append((r, c));
			c += 1;
		r += 1;
	return (nbrs, locs);

def createMat(ind, fi):
	fil = open(fi, 'r');
	whole = [];
	for line in fil:
		line = line.strip('\n');
		puzzle = [];
		for ch in line:
			puzzle.append(ch);
		whole.append(puzzle);
	puzzle = whole[ind];
	matrix = [];
	for r in range(0, 73, 9):
		temp = [];
		for c in range(0, 9):
			temp.append(puzzle[r+c]);
		matrix.append(temp);
	return matrix;


def findPos(nbrs, locs): #returns the position dictionary which has possibiliies at each unknown location
	posMatrix = {};
	for val in locs:
		allPos = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
		r = val[0];
		c = val[1];
		nbrLst = nbrs[val];
		for i in nbrLst:
			allPos.remove(i);
		posMatrix[(r, c)] = allPos;
	return posMatrix;


def fill(posMatrix, matrix):
	if isSolved(matrix):
		disp(matrix)
		return True;
	else:
		count = 0;
		for key in posMatrix:
			if count == 0:
				mink = key;
				count += 1;
			elif len(posMatrix[mink]) > len(posMatrix[key]):
				mink = key;
		if len(posMatrix) > 0:
			pos = posMatrix[mink]
			r = mink[0];
			c = mink[1];
			for val in pos:
				tempM = deepcopy(matrix);
				tempM[r][c] = val;
				(nbrs, locs) = findNbrs(tempM);
				tempP = findPos(nbrs, locs);
				x= fill(tempP, tempM);
				if x : return x
		return False


def disp(matrix):
	print('');
	print('');
	for val in matrix:
		print(val);


matrix = createMat(0, 'test.txt');
disp(matrix);
(nbrs, locs) = findNbrs(matrix);
posMatrix = findPos(nbrs, locs);
fill(posMatrix, matrix);

