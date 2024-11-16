# Using Python List
is_prime = [True for i in range(n + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(2*i, n + 1, i):
            is_prime[j] = False      
primes = [i for i, j in enumerate(is_prime) if j == True] + [0]

# Using Python Set
primes = {i for i in range(2, n + 1)}
for i in range(2, int(n**0.5) + 1):
    if i in primes:
        primes -= {j for j in range(2*i, n + 1, i)}
