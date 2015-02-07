########################
# Name: Sahith Malyala #
#     Date: 2/7/14 	   #
#       Period: 1 	   #
########################

def returnNewLetter(let, times):	#appropriately changes each letter 
	if times < 0:
		newLetter = ord(let) - ((-1*times) % 26);
	else:
		newLetter = ord(let) + (times % 26);
	if times > 0:
		if newLetter > 122:
			newLetter = (newLetter % 122) + 96;
		elif newLetter > 90 and ord(let) < 91:
			newLetter = (newLetter % 90) + 64;
	elif times < 0:
		if newLetter < 65:
			newLetter = 25 - (64 - newLetter) + 65;
		elif newLetter < 97 and ord(let) > 96:
			newLetter = 25 - (96 - newLetter) + 97;
	return chr(newLetter);

def returnNewString(stng, times):	#runs through string and calls returnNewLetter function on each letter
	newString = "";
	for letter in stng:
		if (64 < ord(letter) and ord(letter) < 91) or (96 < ord(letter) and ord(letter) < 123):
			newString += returnNewLetter(letter, times);
		else:
			newString += letter;
	return newString;

def main():		#runs the program
	stringToShift = "CcCcC!";
	timesToShift = -54;
	print(returnNewString(stringToShift, timesToShift));

main();