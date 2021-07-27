# order, immutable, allows duplicates

mytuple = ("apple", "banana", "cherry", 24)
print(mytuple) # ('apple', 'banana', 'cherry', 24)

# from a list
mytuple3 = mytuple[:]
mytuple2 = tuple(["apple", "banana", "cherry", 24, "apple"])
print(mytuple2) # ('apple', 'banana', 'cherry', 24, 'apple')
print(mytuple2[3]) # 24
print(mytuple3) # ('apple', 'banana', 'cherry', 24, 'apple')