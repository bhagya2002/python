# dictionaries
# stores information in key-value pairs
# to create a dictionary use { }

# setting a key for each value
# each key (on the left) must be unique. keys can be any number or string just have to be unique
monthConverstions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Decemeber"
}

# print a value from the key
print(monthConverstions["Nov"])

# using .get() you can set a default if a key entered is not found
print(monthConverstions.get("Luv", "Not a valid key"))
