from re import findall
from itertools import permutations

puzzle = 'DOG * CAT == FIGHT'
puzzle = puzzle.upper();
words = findall('[A-Z]+', puzzle);
begin = set(w[0] for w in words);
keys = ''.join(begin) + ''.join(set(''.join(words))-begin);
for values in permutations('1234567890', len(keys)):
	values = ''.join(values);
	table = str.maketrans(keys, values);
	equation = puzzle.translate(table);
	if '0' not in values[:len(begin)]:
		if eval(equation):
			print('---', equation);
			solutionFound = True;

if not solutionFound:
	print('No solutions exist');
else:
	print('All solutions have been found');

