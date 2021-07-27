# sets: unordered, mutable, no duplicates

myset = {1, 2, 3, 1, 2} # no duplicates allowed
print(myset) # {1, 2, 3}

myset1 = set([1, 2, 3, 4, 1, 2, 3, 4]) # turn list into a set and it removes duplicates
print(myset1) # {1, 2, 3, 4}

myset2 = set("Hello") # unordered
print(myset2) # {'e', 'H', 'l', 'o'}

myset3 = set() # empty set
myset3.add(1) # add 1 to set
myset3.add(2) # add 2 to set
myset3.add(3) # add 3 to set

myset3.discard(3) # remove 3 from set
print(myset3)

myset3.add(3) # add 3 to set

print(myset3.pop()) # remove and return an arbitrary element from set

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # union of two sets (adds two sets
print(u) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens) # intersection of two sets (only common elements)
print(i) # empty set()

i1 = odds.intersection(primes) # intersection of two sets (only common elements)
print(i1) # {3, 5, 7}

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}

diff = a.difference(b) # elements in a but not in b
print(diff) # {4, 5, 6, 7, 8, 9}

symdiff = a.symmetric_difference(b) # elements in either a or b but not both
print(symdiff) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

a.update(b) # add all elements from b to a
print(a) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}

a.intersection_update(b) # set a to only common elements of a and b
print(a) # {1, 2, 3}

a = {1, 2, 3, 4, 5, 6 }
b = {1, 2, 3}

print(b.issubset(a)) # b is a subset of a: True
print(b.issuperset(a)) # b is a superset of a: False

# to copy a set, use the copy() method

# frozenset is immutable (cannot oadd or remove elements)