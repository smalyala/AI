from random import randint
def main():
	drawers = [['G', 'G'], ['S', 'S'], ['G', 'S']];
	success = 0;
	count = 0;
	for i in range(10000):
		chosen = drawers[randint(0, 2)];
		coin = randint(0, 1);
		other = 1;
		if coin:
			other = 0;
		if chosen[coin] == 'G':
			count += 1;
			if chosen[other] == 'G':
				success += 1;
	print((success+0.0)/count);
main();
