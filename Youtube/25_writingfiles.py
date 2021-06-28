# writing to a file

# "a" means appending (adding text at the end)
# if you say "w" for write then that means that the files is override
employee_file = open("files/employees1.txt", "a")

# \n is used for newline
employee_file.write("\nKelly - Customer Service")

employee_file.close()