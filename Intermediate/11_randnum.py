import random # generate pusedo-random

a = random.random()
print(a) # random float number form 0 to 1

b = random.uniform(1, 10)
print(b) # random float number from 1 to 10

c = random.randint(1, 10)
print(c) # random integer number from 1 to 10 (with upper bound included)

d = random.randrange(1, 10)
print(d) # random integer number from 1 to 10 (with upper bound NOT included)

e = random.normalvariate(0, 1)
print(e) # picks a value from the normal distribution of mean 0 and the std of 1

mylist = list("ABCDEFGH")
f = random.choice(mylist) # picks a random letter from this list
print(f)
g = random.sample(mylist, 3) # picks a specified number of random letters from this list (unique)
print(g)
h = random.choices(mylist, k = 3) # picks a specified number of random letters from this list (can be multiple of the same ones)
print(h)
random.shuffle(mylist) # shuffles the entire list
print(mylist)

random.seed(1) # same as second last, can be reproduced
print(random.random())
print(random.randint(1, 10))

random.seed(2) # same as last they can be reproduced
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets # truely secret

i = secrets.randbelow(10)
print(i) # print number from 0-10, 10 NOT included

j = secrets.randbits(4)
print(j) # get any number with 4 bits (4 random binaray values) from 0-15

k = secrets.choice(mylist)
print(k) # get any random value from the list


import numpy as np # used for random array stuff

l = np.random.rand(3)
print(l) # 3 random floats in the array

m = np.random.rand(3,3)
print(m) # 3x3 random floats in the array

n = np.random.randint(0, 10, 3)
print(n) # 3 random ints in an array

o = np.random.randint(0, 10, (3, 4))
print(o) # 4x3 random ints in an matrix array

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr) # matrix array
np.random.shuffle(arr)
print(arr) # shuffles the column only from the rows