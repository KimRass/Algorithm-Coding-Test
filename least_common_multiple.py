lcm = 1
for i in primes:
    while A%i == 0 or B%i == 0:
        lcm *= i
        if A%i == 0:
            A //= i
        if B%i == 0:
            B //= i
