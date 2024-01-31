# condition with boolean
is_correct = True
if is_correct:
    print("Correct")  # Correct
else:
    print("Incorrect")

# condition with None. This will result to False, because None is falsy value. Other falsy values are empty string and 0
cart_items = None
if cart_items:
    print("Some cart items")
else:
    print("No cart items")  # No cart items

food = "kiwi"
if food == "apple":
    print("Healthy")
elif food == "kiwi":
    print("Delicious")  # Delicious
else:
    print("Unknow food")

speed = 59
if speed >= 50 and speed <= 100:
    print("Ok")  # Ok
else:
    print("Not ok")

# not operator will toggle the value
is_allowed = False
if not is_allowed:
    print("It's allowed")  # It's allowed

# value and reference comparison
# below 2 lists have equal values, but they are stored in different places in the memory and have different reference
# 'is' is similar to '===' in javascript
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False

# example with ternary operator
my_value = 9
print('Nine') if my_value == 9 else print('Not Nine') # Nine
