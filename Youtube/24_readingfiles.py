# reading files

# openning files

# good practise to store open file in a variable
employee_file = open("files/employees.txt", "r")


# print(employee_file.readable()) # checks if the file can be read (boolean answer)
# print(employee_file.readline()) # reads and displays one line at a time
# print(employee_file.readline()) # reads and displays one line at a time
# print(employee_file.read()) # reads the whole txt file
# print(employee_file.readlines()[1:3]) # reads the file and puts it in a LIST (you can use indexes to pick different lines)

for employee in employee_file.readlines():
    print(employee)

# make sure to close the file
employee_file.close()