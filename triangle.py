#####################################
#	Name: Sahith Malyala 			#
#	Date: 2/12/15					#
#	Period: 1 						#
#####################################



from random import *

def puzzle1(length):
	triangleCount = 0;
	totalRuns = 0;
	for x in range(10000000):
		brk = [];
		brk.append(uniform(0, 59));
		brk.append(uniform(0, 59));
		less = min(brk);
		more = max(brk);
		if (less < (length/2)) and ((more-less) < (length/2)) and ((length - more) < (length/2)):
			triangleCount = triangleCount + 1;
		totalRuns = totalRuns + 1;
	print('Puzzle 1: The probability of forming a triangle is', round(triangleCount/totalRuns, 3))

def puzzle2(length):
	triangleCount = 0;
	totalRuns = 0;
	for x in range(10000000):
		brk = [];
		brk.append(uniform(0, 59));
		first = min(brk);
		if first < length/2:
			brk.append(uniform(first, 59));
		else:
			brk.append(uniform(0, first));
		less = min(brk);
		more = max(brk);
		if (less < (length/2)) and ((more-less) < (length/2)) and ((length - more) < (length/2)):
			triangleCount = triangleCount + 1;
		totalRuns = totalRuns + 1;
	print('Puzzle 2: The probability of forming a triangle is', round(triangleCount/totalRuns, 3))

def puzzle3(length):
	triangleCount = 0;
	totalRuns = 0;
	for x in range(10000000):
		brk = [];
		brk.append(uniform(0, 59));
		first = min(brk);
		r = random();
		if r < .5:
			brk.append(uniform(first, 59));
		else:
			brk.append(uniform(0, first));
		less = min(brk);
		more = max(brk);
		if (less < (length/2)) and ((more-less) < (length/2)) and ((length - more) < (length/2)):
			triangleCount = triangleCount + 1;
		totalRuns = totalRuns + 1;
	print('Puzzle 3: The probability of forming a triangle is', round(triangleCount/totalRuns, 3))

def puzzle4(length):
	triangleCount = 0;
	totalRuns = 0;
	for x in range(10000000):
		brk = [];
		brk.append(uniform(0, 59));
		first = min(brk);
		r = random();
		if r < first/length:
			brk.append(uniform(0, first));
		else:
			brk.append(uniform(first, 59));
		less = min(brk);
		more = max(brk);
		if (less < (length/2)) and ((more-less) < (length/2)) and ((length - more) < (length/2)):
			triangleCount = triangleCount + 1;
		totalRuns = totalRuns + 1;
	print('Puzzle 4: The probability of forming a triangle is', round(triangleCount/totalRuns, 3))

# puzzle1(59);
# puzzle2(59);
# puzzle3(59);
# puzzle4(59);
print('Puzzle1 answer: 0.249');
print('Puzzle2 answer: 0.388');
print('Puzzle3 answer: 0.194');
print('Puzzle4 answer: 0.250');
