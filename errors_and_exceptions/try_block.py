x = 5

try:
    if not type(x) is str:
        raise TypeError("Only strings allowed")
except Exception as error:
    print(error)
finally:
    print("This text will always be printed")
    