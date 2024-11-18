import sys

sys.setrecursionlimit(10**9)


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:    
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
