stack = [0]
nges = [-1 for _ in range(len(arr))]
i = 1
while i < len(arr):
    while stack:
        popped = stack.pop()
        if arr[i] > arr[popped]:
            nges[popped] = i
        else:        
            stack.append(popped)
            break
    stack.append(i)
    i += 1