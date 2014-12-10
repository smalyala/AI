from random import choice
import Trie

def printGhostDirections():
	print(' +------------------------------------+');
	print(' |    Welcome to the game of GHOST.   |');
	print(' |    The human goes first. Enter     |');
	print(' |    your letters in the pop-up      |');
	print(' |    dialog boxes. Good luck.        |');
	print(' +------------------------------------+');

def requestAndCheckHumanMove(root, stng):
	stng += input('HUMAN, enter your character: ').lower()[0];
	print(' ', stng);
	if root.search(stng) == True:
		print('------------------------------------------');
		print(' HUMAN LOSES because "', stng, '" is a word.', sep = '');
		print('---------------< GAME OVER >--------------');
		exit();
	if root.fragmentInDictionary(stng) == False:
		print('------------------------------------------');
		print(' HUMAN LOSES because "', stng, \
			  '"\n does not begin any word.', sep = '');
		print(" [The computer's word was ", '"', \
			    spellWordFromString(root, stng[0:-1]), '".]', sep = '');
		print('---------------< GAME OVER >--------------');
		exit();
	return stng;

def requestAndCheckComputerMove(root, stng):
	stng += searchForNextLetter(root, stng);
	print(' ', stng, '<-- computer replied');
	if root.search(stng) == True:
		print('------------------------------------------');
		print(' COMPUTER LOSES because "', stng, '" is a word.', sep = '');
		print('---------------< GAME OVER >--------------');
		exit();
	return stng;

def createTrieFromDictionaryFile():
	file1 = open('GhostDictionary.py');
	root = Trie.Node('*');
	for word in file1:
		root.insert(word.lower().strip());
	file1.close();
	return root;

def randomChild(self):
	children = self.children;
	return choice(list(children.keys()));

def searchForNextLetter(self, stng):
	if len(stng) == 0:
		return randomChild(self);
	val = stng[0];
	if val in self.children:
		return self.children[val].search(stng[1:]);
	else:
		return None;

def fragmentInDictionary(self, stng):
	if len(stng) == 0:
		return True;
	val = stng[0];
	if val in self.children:
		return self.children[val].search(stng[1:]);
	else:
		return False;

def main():
	root = createTrieFromDictionaryFile();
	printGhostDirections();
	stng = '';
	while True:
		stng = requestAndCheckHumanMove(root, stng);
		stng = requestAndCheckComputerMove(root, stng);

if __name__ == '__main__':
	main();