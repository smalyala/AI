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

def crMat(ind, fi):
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


def fill(posMatrix, matrix, count):
	if isComplete(matrix):
		disp(matrix);
	if isSolved(matrix):
		disp(matrix)
		print('done')
		return matrix;
	for key in posMatrix:
		r = key[0];
		c = key[1]
		pos = posMatrix[key];
		for val in pos:
			tempM = matrix[:];
			tempM[r][c] = val;
			(nbrs, locs) = findNbrs(tempM);
			tempP = findPos(nbrs, locs);
			return fill(tempP, tempM, count);

def disp(matrix):
	print('');
	print('');
	for val in matrix:
		print(val);

def isComplete(matrix):
	for r in matrix:
		for c in r:
			if c == '.':
				return False;
	return True;

def kep(count):
	return count + 1;


matrix = crMat(9, 'sudokuMedium.txt');
disp(matrix);
(nbrs, locs) = findNbrs(matrix);
posMatrix = findPos(nbrs, locs);
fill(posMatrix, matrix, 0);
