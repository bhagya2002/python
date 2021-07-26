# order, immutable, allows duplicates

mytuple = ("apple", "banana", "cherry", 24)
print(mytuple) # ('apple', 'banana', 'cherry', 24)

# from a list
mytuple2 = tuple(["apple", "banana", "cherry", 24, "apple"])
print(mytuple2) # ('apple', 'banana', 'cherry', 24, 'apple')
print(mytuple2[3]) # 24