def reverseLst(Lst):
	if L > 0:
		return [n for n in reversed(Lst)];
	else:
		return None;
#-------------------------------------------------------------------

def main():
#---Method 1. Use the built-in reverse function.
	Lst1 = [1,2,3,4,5,];
	Lst2 = Lst1[:];
	Lst2.reverse();
	print('Method 1. ', Lst1, Lst2);

#-------------------------------------------------------------------
#---Method 2. Use the built-in reversed function.
	Lst1 = [1,2,3,4,5,];
	Lst2 = list(reversed(Lst1));
	print('Method 2. ', Lst1, Lst2);

#-------------------------------------------------------------------
#---Method 3. Use slicing only.
	Lst1 = [1,2,3,4,5,];
	Lst2 = Lst1[::-1];
	print('Method 3. ', Lst1, Lst2);

#-------------------------------------------------------------------
#---Method 4. Use a for loop that works on this swap principle: a,b 
#   = b,a.
	Lst1 = [1,2,3,4,5,];
	L = len(Lst1);
	Lst2 = Lst1[:];
	for n in range(L//2):
		temp = Lst2[n];
		Lst2[n] = Lst2[L-n-1];
		Lst2[L-n-1] = temp;
	print('Method 4. ', Lst1, Lst2);

#-------------------------------------------------------------------
#---Method 5. Use a for loop (not comprehension) that runs backward
#   and copies each element in Lst1 to Lst2.
	Lst1 = [1,2,3,4,5,];
	Lst2 = [];
	for n in reversed(Lst1):
		Lst2.append(n);
	print('Method 5. ', Lst1, Lst2);

#-------------------------------------------------------------------
#---Method 6. Same as method 5, except it uses a list comprehension.
	Lst1 = [1,2,3,4,5,];
	L = len(Lst1);
	if L > 0:
		Lst2 = [n for n in reversed(Lst1)]
	print('Method 6. ', Lst1, Lst2);
#-------------------------------------------------------------------
#---Method 7. This time, place method 6 in a function. Anticipate
#   what you can be criticized for even if your function works
#   perfectly.
	Lst1 = [1,2,3,4,5,];
	Lst2 = reverseLst(Lst1);
	print('Method 7. ', Lst1, Lst2);
####################################################################

main();