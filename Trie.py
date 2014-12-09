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
		print(self.children);
		if '$' in self.children and self.value != '*' and len(stng) == 0:
			return True;
		val = stng[0];
		print(val);
		if val in self.children:
			print('recur');
			return self.children[val].search(stng[1:]);
		else:
			print('did not find')
			return False;
		print('why here')


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
	print('SEARCH:', root.search('dogn'));
	printElapsedTime();

def printElapsedTime():
	print('\n---Total run time = ', round(clock()-startTime, 2), 'seconds.');

if __name__ == '__main__': startTime = clock(); main()
