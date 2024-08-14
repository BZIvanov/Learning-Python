sum_nums = lambda a, b: a + b

print(sum_nums(2, 3))  # 5

nums_list = [1, 3, 5, 4, 9]

squared_nums = map(lambda num: num * num, nums_list)

print(list(squared_nums))  # [1, 9, 25, 16, 81]
