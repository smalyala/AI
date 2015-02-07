########################
# Name: Sahith Malyala #
#     Date: 2/7/14 	   #
#       Period: 1 	   #
########################

def returnNewLetter(let, times):					#appropriately changes each letter 
	if times < 0:										#bypasses limitations of python modulo
		newLetter = ord(let) - ((-1*times) % 26);
	else:	
		newLetter = ord(let) + (times % 26);
	if times > 0:										#ensures circular nature forward
		if newLetter > 122:									#deals with lowercase letters
			newLetter = (newLetter % 122) + 96;
		elif newLetter > 90 and ord(let) < 91:				#deals with uppercase letters
			newLetter = (newLetter % 90) + 64;
	elif times < 0:										#ensures circular nature backward
		if newLetter < 65:									#deals with uppercase letters
			newLetter = 25 - (64 - newLetter) + 65;
		elif newLetter < 97 and ord(let) > 96:				#deals with lowercase letters
			newLetter = 25 - (96 - newLetter) + 97;
	return chr(newLetter);

def returnNewString(stng, times):		#runs through string and calls returnNewLetter function on each letter
	newString = "";
	for letter in stng:						#checks each character in string
		if (64 < ord(letter) and ord(letter) < 91) or (96 < ord(letter) and ord(letter) < 123):		#if letter
			newString += returnNewLetter(letter, times);
		else:												#if not letter
			newString += letter;
	return newString;

def main():			#runs the program
	stringToShift = "Cheer!";
	timesToShift = 7;
	print(returnNewString(stringToShift, timesToShift));

main();