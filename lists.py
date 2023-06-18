fruits = ["apple", "kiwi", "banana"]
print(len(fruits))  # 3
print(fruits[1])  # kiwi
print(fruits[-1])  # banana
print("kiwi" in fruits)  # True

for fruit in fruits:
    print(f"Delicious {fruit}")

fruits.append("orange")
print(len(fruits))  # 4
print(fruits[-1])  # orange

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2])  # [2, 4, 6]

# NESTED LIST

nested_items = [[1, 2, 3], [4, 5, 6]]
print(nested_items[1][1])  # 5

# LIST COMPREHENSION

values = [1, 2, 3]
updated_values = [x * 3 for x in values]
print(updated_values)  # [3, 6, 9]

username = "Iva"
print([ch.upper() for ch in username])  # ['I', 'V', 'A']
