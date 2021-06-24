# List functions

lucky_number = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jimmy", "Jimmy", "Oscar", "Tim"]

# add a value to the end of a list
friends.extend(lucky_number)

# add ONE more value to the list
friends.append("Creed")

# add value in the middle somewhere
friends.insert(1, "Kelly") # at the index add a value and push right to the right

# remove value from the list
friends.remove("Tim")

# remove everything from the list
# friends.clear()

# remove the last element of the list
friends.pop()

print(friends)

# get index of the value we want
print(friends.index("Oscar"))

# counts the number of occurances of smth
print(friends.count("Jimmy"))

# sort the list
# friends.sort() # sorts in alphabetical order
print(friends)

# reverse the list
lucky_number.reverse()
print(lucky_number)

# copy the list
friends2 = friends.copy()
print(friends2)