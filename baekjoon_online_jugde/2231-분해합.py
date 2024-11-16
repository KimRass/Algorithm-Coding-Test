# Source: https://www.acmicpc.net/problem/2231

def solve(n):
    i = n - 1
    minim = n
    lim = 0
    while i > lim and i > 0:
        arr = list(map(int, str(i)))
        res = i + sum(arr)
        if res == n:
            if i < minim:
                minim = i
                lim = i - 53
            i -= (arr[-1] + 1)
        else:
            i -= 1
    return minim if minim != n else 0


if __name__ == "__main__":
    # n = 216
    n = int(input())
    answer = solve(n)
    print(answer)
