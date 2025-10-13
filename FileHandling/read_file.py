my_file = open("text-file.txt", "r")
# will print the file content
print(my_file.read())

# here we will have no text returned, because the cursor is at the end of the file
print(my_file.read())

# this way we can return the cursor back at the start of the file
my_file.seek(0)

# will print the file content
print(my_file.read())

print(my_file.closed)  # False
# it is important to close our files after we are done working with them
my_file.close()
print(my_file.closed)  # True
