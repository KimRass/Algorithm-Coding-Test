for i in range(len(arr)):
    min_j = i
    for j in range(i, len(arr)):
        if arr[j] < arr[min_j]:
            min_j = j
    arr[i], arr[min_j] = arr[min_j], arr[i]
