# for loops
# repetitive loops that run an x numebr of times
# for (index name) in (smth):

# loop through the word "soccer academy" and print each letter
for letter in "Soccer Academy":
    print(letter)

# loop through an array
friends = ["Jim", "Karen", "Tom"]
for friend in friends:
    print(friend)

# loops from 0-10 (excluding 10)
for index in range(10):
    print(index)

# from 3-10 (excluding 10)
for index in range(3, 10):
    print(index)


# taking each index in the array and displaying it
for index in range(len(friends)):
    print(friends[index])

# more complec for loop
for indexer in range(5):
    if indexer == 0:
        print("first iteration")
    else:
        print("not first")