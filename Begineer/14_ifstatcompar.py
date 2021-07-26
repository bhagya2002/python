# ifstatements and comparisons
# you can compare any data type (bool, num, str, etc.)
# >= -> greater than or equal to
# <= -> less than or equal to
# == -> equals to 
# != -> not equal to

# to check for biggest number from three numbers passed in as parameters
def max_num(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

print(max_num(3, 4, 5))