mem = [[[0, ""] for _ in range(len(arr2) + 1)] for _ in range(len(arr1) + 1)]

maxim = 0
LCS = ""
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            mem[i + 1][j + 1][0] = mem[i][j][0] + 1
            mem[i + 1][j + 1][1] = mem[i][j][1] + arr1[i]
        else:
            if mem[i][j + 1][0] > mem[i + 1][j][0]:
                mem[i + 1][j + 1][0] = mem[i][j + 1][0]
                mem[i + 1][j + 1][1] = mem[i][j + 1][1]
            else:
                mem[i + 1][j + 1][0] = mem[i + 1][j][0]
                mem[i + 1][j + 1][1] = mem[i + 1][j][1]
        if mem[i + 1][j + 1][0] > maxim:
            maxim = mem[i + 1][j + 1][0]
            LCS = mem[i + 1][j + 1][1]
