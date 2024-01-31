# NUMBER

apples = 3
bananas = 5
fav_fruits = apples + bananas
print(fav_fruits)  # 8
# this is how we can check the type of the value
print(type(fav_fruits))  # <class 'int'>

# this is how we can assign multiple variables at once
a, b, c = 10, 15, 20
print(a + c - b)  # 15

# example with float type
print(type(8.1))  # <class 'float'>

# BOOLEAN

# example of boolean usage
is_correct = True
has_items = False

# STRING

# string formatting example
username = "Iva"
print(type(username))  # <class 'str'>
print(f"Hello, {username}")  # Hello, Iva

# multiline text
mulitlines_text = '''
This is 
    multi line
text.
'''
print(mulitlines_text)

# NONE

# example of None usage, it is similar to null in javascript
cart_items = None
print(type(cart_items))  # <class 'NoneType'>
