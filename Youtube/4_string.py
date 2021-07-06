#strings
# "\n" -> newline
# "\t" -> tab
# "\\" -> backslash
# "\"" -> quote

# indexing starts at 0
# all these are . functions
# count(item) -> counts the number of occurances
# find(item) -> find the index of the item
# split(char) -> split the string from the char and shift everything right
# upper() -> make string uppercase
# lower() -> make string lowercase
# replace(old, new, max) -> replace smth
# isdigit() -> true/false to see if variable is a digit
# islower() -> true/false to see if the variable is lowercase
# etc...

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
# print(phrase.index("A"))

# replace in a string
print(phrase.replace("Tom", "Parents"))
print(phrase)

a = 23
b = 100
print("My numbers are {1} and {0}".format(a, b))

# formatting
# field-width {:15} -> right justified (the number specifys the char field width)
# field-width {:<15} -> left justified "<"
# pad with 0's {:015} (the 0 specifies padd the empty spaces with 0 and have a field length of 15
# digits after decimal point {:015.2f} (the number after the "." is the number of sig figs after the decimal

x_is = 15.789375439535
print("the number is {0:025.3f}.".format(x_is)) # 25 field width w/ 3 sig fig after decimal padding w 0's, right 
print("the number is {0:<20.2f}.".format(x_is)) # 20 field width w/ 2 sig fig after decimal no padding, left 