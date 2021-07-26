# returns
# used when you want information back from a function ("return information")

def cube(num):
    return num * num * num # w/o the keyword return there is no way for it to know that information needs to be sent out

# after the return no code in the function will run! its a break out of the function

print(cube(3)) # just display it or...
result = cube(3) # you can also store the answer from the function
print(result) # display that answer