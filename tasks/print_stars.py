# print n stars per line starting from 1 to n and then from n - 1 to 1


def print_stars(n):
    for x in range(1, n + 1):
        print(" ".join("*" * x))
    for x in range(n - 1, 0, -1):
        print(" ".join("*" * x))


print_stars(5)
