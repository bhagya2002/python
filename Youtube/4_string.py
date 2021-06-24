#strings

phrase = "Tom"

print("John Anderson")

# to insert a newline use \n
print("John\Anderson")

# to use a quotation mark use \" (escape character) - any char after this is valid
print("John \"A\" Anderson")

# concatination
print(phrase + " is a cool guy!")

# string functions use "."
print(phrase.islower())

# length of a string
print(len(phrase))

# get individual characters, string is indexed starting from 0
print(phrase[0])

# find form a string
print(phrase.index("A"))

# replace in a string
print(phrase.replace("Tom", "Parents"))
print(phrase)