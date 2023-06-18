for ch in "Hello":
    print(ch)  # will print letters one by one

print("-" * 20)

for x in range(1, 5):
    print(x)  # will print the numbers 1 2 3 4

print("-" * 20)

n = 1
while n < 5:
    print(n)  # will print the numbers 1 2 3 4
    n += 1

print("-" * 20)

m = 1
while True:
    print(m)  # will print the numbers 1 2 3
    if m == 3:
        break
    m += 1
