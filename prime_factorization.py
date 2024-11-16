m = int(n**0.5)
primes = {i for i in range(2, m + 1)}
for i in range(2, int(m**0.5) + 1):
    if i in primes:
        primes -= {j for j in range(2*i, m + 1, i)}

prime_facts = list()
for i in sorted(list(primes)):
    while n%i == 0:
        n //= i
        prime_facts.append(i)
if n != 1:
    prime_facts.append(n)
