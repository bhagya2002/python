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

listed = [1, 2, 3, 4, 5, 6]

listed.append(7) # add 7 to the end of the list
print(listed)

listed.insert(4, 4) # [1, 2, 3, 4, 4, 5, 6, 7]
print(listed)

# removes the last time in the list
listed.pop() # [1, 2, 3, 4, 4, 5, 6]
print(listed)

# removes the item at index 1
listed.pop(1) # [1, 3, 4, 4, 5, 6]
print(listed)

# removes the first occurance of "3" in this case
listed.remove(3) # [1, 4, 4, 5, 6]
print(listed)

# reveres the list
listed.reverse() # [6, 5, 4, 4, 1]
print(listed)

# counts the number of occurances in the list
counter = listed.count(4) 
print(counter) # 2

# get the index of the first occurance of the number in the list
indexer = listed.index(5)
print(indexer) # 1

# splits the string into individuals chars and stores in a list
stringed = list("CMPUT")
print(stringed)

# split the string wherever there is a "," and store in a list
number = "1,2,3,,5".split(",")
print(number)

# joined it together seperated by " "
joined = ' '.join(['1', '2', '3', '4', '5']) # 1 2 3 4 5
print(joined)

# joined it together seperated by ""
joined1 = ''.join(['1', '2', '3', '4', '5']) # 12345
print(joined1)