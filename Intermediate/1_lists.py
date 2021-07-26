mylist = [0] * 5
print(mylist) # [0, 0, 0, 0, 0]

mylist2 = [1, 2, 3, 4, 5]
newlist = mylist2 + mylist
print(newlist) # [1, 2, 3, 4, 5, 0, 0, 0, 0]

listed =[1,2,3,4,5,6,7,8,9]
started = listed[0:3] # unspecified start or end means all the way to the left or the right
started2 = listed[::2] # every other item
print(started) # [1, 2, 3]
print(started2) # [1, 3, 5, 7, 9]

listorg = ['banana', 'cherry', 'apple']
listcopy = listorg.copy() # makes a copy of the list
listcopy.append('orange') # adds orange to the copy
print(listcopy) # ['banana', 'cherry', 'apple', 'orange']
print(listorg) # ['banana', 'cherry', 'apple']

# make a list and for loop it at once
line1 = [1, 2, 3, 4, 5, 6]
linelooped = [i*i for i in line1]
print(linelooped) # [1, 4, 9, 16, 25, 36]