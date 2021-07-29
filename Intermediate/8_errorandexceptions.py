# Errors and Exceptions

# a = 5 + "10" -> type error

# import somerandommodule -> module error

# a = 5
# b = c -> name error

# f = open("file.txt", "r") -> file not found error

# raising your own exceptions with RAISE
from typing import final


x= -5
if x < 0:
    raise Exception("x should be a postive number")

# exception with a for loop
# assert (operation), (message) -> exception when the operation is false
assert (x >= 0), "x should be a postive number"

# try this first
try:
    a = 5 / 0
# if an error occurs, execute this
# except:
    # print("an error happened")

# or you can print out the exception raised
except Exception as e:
    print(e) # ZeroDivisionError
else:
    print("everything is fine")
# runs no matter what 
finally:
    print("cleaning up..")
