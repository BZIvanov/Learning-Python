num = 0


# here we can use the variable num outside of the function scope, because we are not manipulating it
def get_num():
    return num


print(get_num())


count = 0


# with the keyword global, the increment function will search for count variable in its scope and will throw an error
def increment():
    global count
    count += 1
    return count


print(increment())
