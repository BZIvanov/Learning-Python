person = {"name": "Iva", "age": 29, "is_online": True}
print(person["name"])  # Iva
print(person.get("age"))  # 29

for k, v in person.items():
    print(k, v)

print("status" in person)  # False

# DICTIONARY COMPREHENSION

info_data = {"type": "text", "value": "abc", "style": "bold"}
upper_info_data = {k.upper(): v.upper() for k, v in info_data.items()}
print(upper_info_data)  # {'TYPE': 'TEXT', 'VALUE': 'ABC', 'STYLE': 'BOLD'}

nums = [1, 2, 3]
text_nums = {num: ("even" if num % 2 == 0 else "odd") for num in nums}
print(text_nums)  # {1: 'odd', 2: 'even', 3: 'odd'}
