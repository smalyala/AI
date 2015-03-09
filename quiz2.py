from random import *
r = choice([-1, 1]);
print('#1: ', r);
if random() > .5: r = -1;
else: r = 1;
print('#2: ', r);
r = randrange(-1, 3, 2);
print('#3: ', r);
r = sample([-1, 1], 1);
print('#4: ', r[0]);
r = [-1, 1];
shuffle(r);
print('#5 : ', r[0]);
