# lists

# "in" asks if smth is in the list
# "len(list_name")" returns the length of the list

# use [] to create a list
# lists can be any type (string, bool, num)
friends = ["Mike", "John", "Tom", "Hank"]

# index of the lists
print(friends[2])
# negative index also exists (go from right to left starting from -1 being right most)
print(friends[-1])

# select a range
print(friends[1:]) # from index 1 to end
print(friends[1:3]) # includes left index and everything in between but not including right index

# get index of a index
print(friends[2][1])

# change index positions
friends[1] = "Carson"
print(friends)

listed = [1, 2, 3, 4, 5, 6]
x = 3 in listed
print(x) # returns true

print(len(listed)) # 6