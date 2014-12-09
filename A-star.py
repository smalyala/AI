#Name: Sahith Malyala
#Date: 9/16/14
#Period: 1

from pickle import load
nbr = load(open('fullList.pkl', 'rb'))

start = input('Start word: ')
finish = input('End word: ')

def findH(word1, word2):
	count = 0;
	j = 0
	while j < 6:
		if word1[j] != word2[j]:
			count += 1
		j += 1
	dCov = 0;
	while parent[word1] != None:
		dCov += 1;
		word1 = parent[word1];
	return dCov * 2 + count;

pq = [];

do = 1;
parent = {};
parent[start] = None;
firstH = findH(start, finish);
pq.append((firstH, start));
wordsUsed = []
now = (0, "")
countT = 0
while now[1] != finish:
	pq.sort();
	now = pq.pop(0);
	countT += 1
	if now[1] not in wordsUsed and now not in pq:
		if now[1] != finish:
			for val in nbr[now[1]]:
				if val not in wordsUsed:
					good = 1;
					for x in pq:
						if val == x[1]:
							good = 0;
					if (good):
						parent[val] = now[1]
						pq.append((findH(val, finish), val))
			if (len(pq) == 0):
				do = 0;
				print('No path exists')
				break;
		else:
			break
		wordsUsed.append(now[1])
if (do):
	path = []
	path.append(finish)
	now = finish
	while parent[now] != None:
		path.append(parent[now])
		now = parent[now]
	path.reverse()
	print(path)
	print("Length: " , len(path))
	print("Pops: " , countT)
