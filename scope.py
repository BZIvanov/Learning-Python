num = 0


# here we can use the variable num outside of the function scope, because we are not manipulating it
def get_num():
    return num


print(get_num())


count = 0


# without the keyword global, the increment function will search for count variable in its scope and will throw an error for not finding it
def increment():
    global count
    count += 1
    return count


print(increment())


# nonlocal is used within a nested function to indicate that a variable refers to a variable in the nearest enclosing scope that is not global.
# it allows you to modify a variable in an outer (but non-global) scope.
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20
        print(x) # 20

    inner_function()
    print(x) # 20

outer_function()
