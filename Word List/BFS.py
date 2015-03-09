from pickle import load
nbr = load(open('fullList.pkl', 'rb'))

start = input('Start word: ')
finish = input('End word: ')

do = 1;
q = [];
parent = {};
parent[start] = None;
q.append(start);
wordsUsed = []
now = ""
count = 0;
while now != finish:
	now = q.pop(0);
	count += 1;
	if now not in wordsUsed and now not in q:
		if now != finish:
			for val in nbr[now]:
				if val not in wordsUsed and val not in q:
					q.append(val)
					parent[val] = now
			if (len(q) == 0):
				do = 0;
				print('No path exists')
				break;
		else:
			break
		wordsUsed.append(now)
if (do):
	path = []
	path.append(finish)
	now = finish
	while parent[now] != None:
		path.append(parent[now])
		now = parent[now]
	path.reverse()
	print(path)
	print(len(path))
	print(count)

