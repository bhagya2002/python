# try/except

try:
    value = 10/0
    number = input("Enter a numer: ")
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")