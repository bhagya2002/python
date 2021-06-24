# better calc mini  assignment
# user chooses operation (+ - * /) from words

num1 = float(input("Enter first number: ")) # convert to float right away (must be a number input)
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "/"):
    print(num1 / num2)
elif (operator == "*"):
    print(num1 * num2)
else:
    print("invalid operator, try again with one of these operators: +, -, /, or *")
