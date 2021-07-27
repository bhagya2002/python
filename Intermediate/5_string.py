# string: ordered, immun=abke, text repsentation

mystring = "Hello World"
print(mystring)

mystring1 = "I\'m a programmer"
print(mystring1)

# you cannot change a string

substring = mystring[0:4]
print(substring) # prints "Hell"

stringed = "        Hello World        "
stripged = stringed.strip()
print(stripged) # prints "Hello World" and takes out the extra spaces

# check if string starts with a specific character .startswith()
# check if string ends with a specific character .endswith()

stringer = list("how are you doing?".split())
print(stringer)

# FORMATS
var = "Tom"
mystring6 = "Hello, %s" % var # placeholder with var
print(mystring6)

var1 = 6
mystring7 = "Hello, %d" % var1 # placeholder with num (whole number unless you said %f)
print(mystring7) #default 6 digits after the decimal unless you say "%.{sig dig}f"

var2 = "Timmy"
varage = 23.946580936
mystring8 = "Hello, {}. You are {:.2f}.".format(var2, varage) # placeholder with num (whole number unless you said %f)
print(mystring8) #default 6 digits after the decimal unless you say "%.{sig dig}f"

# fstrings
mystring8 = f"Hello, {var2}. You are {varage:.2f}." # placeholder with num (whole number unless you said %f)
print(mystring8) #default 6 digits after the decimal unless you say "%.{sig dig}f"