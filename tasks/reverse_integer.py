# Print integer number with reversed digits


# Solution 1
def reverse_integer(num):
    num_str = str(num)

    reversed_str = num_str[::-1]

    reversed_num = int(reversed_str)

    return reversed_num


n = 12345
reversed_number = reverse_integer(n)
print(reversed_number)  # 54321


# Solution 2
number = 12345
reverse_number = 0

while number > 0:
    remainder = number % 10
    reverse_number = reverse_number * 10 + remainder
    number = int(number / 10)

print(reverse_number)  # 54321
