# function
# we use functions when we have to repeat smth a bunch of times

user = input("Enter your name: ")

# to initialize a function use "def + (nameoffunction) + ():"
# rememeber your indent for it to be part of the function
def say_hi():
    print("Hello User")
    # execute code by "nameoffuntion()" shown below

print("First") # first line read
say_hi() # python reads this and jumps to the function (line 7)
print("Last") # last line read 


# you can give a function more information by passing in "parameters" (data from outside the function)
# parameters are passed in the () following the function name
# to tell the function what the data it is we are passing it let u know when u call it (ex. line 22)
def say_hi_to_user(name):
    print("Hi, " + name)

say_hi_to_user(user) # this takes the input from the user and uses that data as the "parameter" for the function
say_hi_to_user("Johnny") # this is made one we can change but is another way to pass in parameters (w/ variables or with any type)

# you can pass in multiple parameters
def say_hi_to_user_age(name, age):
    print("Hi, " + name +"! You're " + age + " years old.")

say_hi_to_user_age(user, "26") 
say_hi_to_user_age("Johnny", "35")
say_hi_to_user_age("Tim", str(70)) # since we cannot use numbers when concatincating we must convert any nums to strings

# default values can be  passed to a parameters