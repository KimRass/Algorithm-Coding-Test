# Implementation
gcd = 1
for i in primes:
    while A%i == 0 and B%i == 0:
        gcd *= i
        A //= i
        B //= i

# Using Euclidean Algorithm
def gcd(a, b):
    if a >= b:
        return b if a%b == 0 else gcd(b, a%b)
    else:
        return a if b%a == 0 else gcd(a, b%a)
