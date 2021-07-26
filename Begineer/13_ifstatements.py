# if statements  -> allows to responds to different data
# run some code if you statement is true or run some other code

is_male = False
is_tall = True

# if (condition):
#   execute this
# else:
#   execture this

if (is_male): # if is_male is equal to True then run this
	print("You are a male")
else: # if is_male is NOT equal to True then run this
	print("You are not a male")


# you can also make combinations of statements
# can use "and" or "or" to combine multiple statements
if (is_male or is_tall): # if is_male or is_tall or both run this
	print("You are a male or tall or both")
else: # if neither is_male or is_tall run this
	print("You are neither a male or tall")


if (is_male and is_tall): # if is_male and is_tall run this
	print("You are a tall male.")
else: # if not is_male or is_tall or both run this
	print("You are not a tall male")


# you can add more conditions with "elif"
# can use "not(variable)" to check if it false
if (is_male and is_tall): # if both run this
	print("You are a tall male.")
elif (is_male and not(is_tall)): # if male but not tall run this
	print("You are a male but not tall")
elif (is_tall and not(is_male)): # if tall but not male run this
	print("You are tall but not a male")
else: # if neither run this
	print("You are neither male or tall")