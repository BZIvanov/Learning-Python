# Print which numbers are prime numbers, starting from 1 to 100


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = []
for num in range(1, 101):
    if is_prime(num):
        primes.append(num)

print(primes)
