mem = [[0 for _ in range(len(string1))] for _ in range(len(string2))]
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            mem[i][j] = mem[i - 1][j - 1] + 1
        else:
            mem[i][j] = 0
