# SIMPLE LIST

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

# with loop

values = [1, 2, 3]
updated_values = [x * 3 for x in values]
print(updated_values)  # [3, 6, 9]

username = "Iva"
print([ch.upper() for ch in username])  # ['I', 'V', 'A']

# with nested loop

nested_loops_comp = [i + j for i in range(2) for j in range(5)]
print(nested_loops_comp) # [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]


fruits = ['kiwi', 'apple', 'banana']
fruits_prices = [3, 1, 2]
fruits_quantities = [4, 5]

sale_options = [
    [fruit, fruit_price * fruit_quantity]
    for fruit in fruits
    for fruit_price in fruits_prices
    for fruit_quantity in fruits_quantities
]
print(sale_options)
# [
#   ['kiwi', 12], ['kiwi', 15], ['kiwi', 4], ['kiwi', 5], ['kiwi', 8], ['kiwi', 10],
#   ['apple', 12], ['apple', 15], ['apple', 4], ['apple', 5], ['apple', 8], ['apple', 10],
#   ['banana', 12], ['banana', 15], ['banana', 4], ['banana', 5], ['banana', 8], ['banana', 10]
# ]

even_odd_nums = [x * 10 if x % 2 == 0 else "None" for x in range(1, 11)]
print(even_odd_nums) # ['None', 20, 'None', 40, 'None', 60, 'None', 80, 'None', 100]
