# functionName = lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5)) # 15

mult = lambda x, y: x * y
print(mult(2, 3)) # 6

print2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# sorts the list above using a function to sort via the y value
print2D_sorted = sorted(print2D, key= lambda x: x[1])

# sorts the list using a function to sorta via the largest sum of the x and y values
print2D_sorted_xy = sorted(print2D, key= lambda x: x[0] + x[1])

print(print2D)
print(print2D_sorted)
print(print2D_sorted_xy)

a = [1, 2, 3, 4, 5, 6]

# MAP -> function that applies to everything specified, ex. a list

# apply a function to each element in a list using the lambda
b = map(lambda x: x * 2, a) # multiples each element by 2
print(list(b)) # have to turn it into a list first for it to be seen

# for loop to do the same thing as above
c = [x * 2 for x in a]
print(c)

# FILTER -> takes a function and if it returns True then return it

d = filter(lambda x: x % 2 == 0, a)
print(list(d))

e = [x for x in a if x % 2 == 0]
print(list(e))

# REDUCE -> repededly applies a function and returns a single value
from functools import reduce

# initialize a value for prod and get a the sum of the prods for list "a"
product_a = reduce(lambda x, prod=1: x * prod, a)
print(product_a)