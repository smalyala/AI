from math import sqrt;

n = 12;

#Problem 1
def fib1(n):
	a = 1;
	b = 1;
	for i in range(1, n-1):
		if n < 3:
			c = a;
			break;
		c = a + b;
		a = b;
		b = c;
	return c;

#Problem 2
def fib2(n, b, c):
	if n < 3:
		return c;
	return fib2(n-1, c, b+c);

def fib3(n):
	a = 1;
	b = 1;
	f = True;
	for i in range(0, n-1):
		if n < 3:
			break;
		if (f):
			b = a + b;
		else:
			a = a + b;
		f = not(f);
	if (n % 2 == 0):
		return a;
	else:
		return b;

def fib4(n, b, c):
	if n < 3:
		return c;
	return fib2(n-1, c, b+c);

def fib7(n):
	return ((((1+sqrt(5))/2)**n) - (((1-sqrt(5))/2)**n))/sqrt(5);

def fib8(n):
	from decimal import Decimal, getcontext;

# print(fib1(n))
# print(fib2(n, 1, 1));
# print(fib3(n));
# print(fib7(n));
