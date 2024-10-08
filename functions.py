# EXAMPLE: Simple self documenting function


def say_hello():
    """Prints the Hello string"""
    print("Hello")


say_hello()
print(say_hello.__doc__)  # Prints the Hello string

# EXAMPLE: Providing arguments to a function


def get_greeting(username):
    return f"Hello, {username}"


greeting = get_greeting("Iva")
print(greeting)  # Hello, Iva

# EXAMPLE: Providing arguments with custom order


def get_names(first, last):
    return f"{first} {last}"


print(get_names(first="Iva", last="Ivanova"))  # Iva Ivanova
print(get_names(last="Ivanova", first="Iva"))  # Iva Ivanova

# EXAMPLE: Collecting all the arguments


# adding a star before the argument name will collect all function arguments in a tuple
def sum_numbers(*args):
    print(type(args))  # <class 'tuple'>
    sum = 0
    for n in args:
        sum += n
    return sum


print(sum_numbers(1, 2, 3, 4, 5))  # 15


# adding two stars before the argument name will collect all function arguments in a dictionary
def list_names(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)  # {'first': 'Iva', 'last': 'Ivanova'}


print(list_names(first="Iva", last="Ivanova"))

# EXAMPLE: Default value for a function


def default_greet(name="World"):
    return f"Hello, {name}!"


print(default_greet())  # Hello, World!
