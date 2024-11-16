arr = [0] + arr

# `mem[i]`: i를 가장 마지막 원소로 갖는 LIS의 길이.
mem = {0:0}
for i in arr[1:]:
    # i를 마지막 원소로 갖는 LIS의 길이는, i보다 작은 값을 마지막 원소로 갖는 LIS의 길이에 1을 더한 값과 같습니다.
    mem[i] = max([v for k, v in mem.items() if k < i]) + 1
print(max(mem.values()))
