# tuple values cannot be reassigned

answer_options = ("yes", "no")
print(type(answer_options))  # <class 'tuple'>
print(answer_options[0])  # yes

nums_tuple = (2, 8, 3, 1, 9)
(first, second, *rest) = nums_tuple
print(first)  # 2
print(second)  # 8
print(rest)  # [3, 1, 9]
