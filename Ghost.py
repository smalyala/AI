def printGhostDirections():
	print(' +------------------------------------+');
	print(' |    Welcome to the game of GHOST.   |');
	print(' |    The human goes first. Enter     |');
	print(' |    your letters in the pop-up      |');
	print(' |    dialog boxes. Good luck.        |');

def requestAndCheckHumanMove(root, stng):
	stng += input('HUMAN, enter your character: ').lower()[0];
	print(' ', stng);
	if root.search(stng) == True:
		print('------------------------------------------');
		print(' HUMAN LOSES because "', stng, '" is a word.', sep = '');
		print('---------------< GAME OVER >--------------'):
		exit();
	if root.fragmentInDictinoary(stng) == False:
		print('------------------------------------------');
		print(' HUMAN LOSES because "', stng, \
			  '"\n does not begin any word.', sep = '');
		print(" [The computer's word was ", '"', \
			    spellWordFromString(root, stng[0:-1]), '".]', sep = '');
		print('---------------< GAME OVER >--------------'):
		exit();
	return stng;

def main():
	root = createTrieFromDictionaryFile();
	printGhostDirections();
	stng = '';
	while True:
		stng = requestAndCheckHumanMove(root, stng);
		stng = requestAndCheckComputerMove(root, stng);

if __name__ == '__main__':
	main();