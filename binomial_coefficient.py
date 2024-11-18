import math

math.factorial(n)//(math.factorial(n - k)*math.factorial(k))


# n*(n - 1)*...*(n - k + 1)/(1*2*...*k)
minim = min(k, n - k)
maxim = max(k, n - k)
res = 1
for i in range(n, maxim, -1):
    res *= i
for i in range(minim, 0, -1):
    res //= i
