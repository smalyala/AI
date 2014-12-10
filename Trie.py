from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

class Node(object):

	def __init__(self, value):
		self.value = value;
		self.children = {};

	def __repr__(self):
		#self.print();
		return '';

	#def print(self, stng):
		#######

	def display(self):
		if self.value == '$': return;
		print('======== NODE ========');
		print('--> self.value     =', self.value);
		print('--> self.children: [', end = '');
		for key in self.children:
			if key != '$':
				print(key, sep = '', end = ', ');
		print(']');
		print('----------------------');
		for char in self.children:
			(self.children[char]).display();

	def insert(self, stng):
		if stng == '':
			self.children['$'] = Node('$');
			return;
		if stng[0] not in self.children:
			p = Node(stng[0]);
			self.children[stng[0]] = p;
			p.insert(stng[1:]);
			return;
		self.children[stng[0]].insert(stng[1:]);

	def search(self, stng):
		if len(stng) == 0 and '$' in self.children:
			return True;
		elif len(stng) == 0:
			return False;
		val = stng[0];
		if val in self.children:
			return self.children[val].search(stng[1:]);
		else:
			return False;


def main():
	root = Node('*');
	root.insert('cat');
	root.insert('catnip');
	root.insert('cats');
	root.insert('catnap');
	root.insert("can't");
	root.insert('cat-x');
	root.insert('dog');
	root.insert('dogs');
	root.insert('dognip');
	root.insert('');
	root.display();
	print('SEARCH:', root.search(""));
	printElapsedTime();

def printElapsedTime():
	print('\n---Total run time = ', round(clock()-startTime, 2), 'seconds.');

if __name__ == '__main__': startTime = clock(); main()
