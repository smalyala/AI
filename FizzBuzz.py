#+-------------------------+
#+  Name: Sahith Malyala   +
#+  Date: 4/7/15           +
#+  Period: 1              +
#+-------------------------+

#--------Part 1-------------

# for x in range(1, 101):
# 	if x % 15 == 0:
# 		print('Fizz and Buzz')
# 	elif x % 3 == 0:
# 		print('Fizz')
# 	elif x % 5 == 0:
# 		print('Buzz')
# 	else:
# 		print(x)

#--------------------------------------
#It worked
#--------------------------------------
# Three reasons why a recruiter might
# not hire a top programmer are the
# programmer might not collaborate
# effectively with others, he/she is
# lazy, and he/she has a strained
# relationship with the boss.

#-------Part 2-------------

# from random import *

# m = [[random()*10 for col in range(3)] for row in range(3)]
# print("Matrix:")
# for row in m:
# 	for col in row:
# 		print("%.2f" % col, end = '  ')
# 	print('')

#------Part 3--------------

from random import *

v = [random()*10 for col in range(4)]
print('Vector:')
for x in v:
	print(x, end='  ')
m = [[random()*10 for col in range(3)] for row in range(4)]
print('')
print('Matrix:')
for row in m:
	for col in row:
		print("%.2f" % col, end = '  ')
	print('')
final = []
for col in range(3):
	val = 0
	i = 0
	for row in m:
		val += v[i] * row[col]
		i+=1
	final.append("%.2f" % val)
print('Resulting vector:')
print(final)
