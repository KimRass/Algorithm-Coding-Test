# M = int(input())
# longs = list(map(int, input().split()))
# N = int(input())
# shorts = list(map(int, input().split()))

M = 4
longs = [30, 40, 50, 25]
N = 10
shorts = [15, 16, 17, 18, 19, 20, 21, 25, 24, 30]


longs.sort(reverse=True)
shorts.sort(reverse=True)

# [25, 30, 40, 50]
# [15, 16, 17, 18, 19, 20, 21, 24, 25, 30]
# [30, 25, 24, 21, 20, 19, 18, 17, 16, 15]
cnt = 0
for long in longs:
    cur_leng = long
    for short in shorts:
        if cur_leng >= short:
            cnt += 1
            cur_leng -= short
            print(long, short)
