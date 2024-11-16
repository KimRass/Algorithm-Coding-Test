def merge(arr1: list, arr2: list) -> list:
    i = j = 0
    merged_arr = []
    while i < len(arr1) and j < len(arr2):  # the merge process takes $O(n)$ time.
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    return merged_arr


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid:]  # Each split takes constant time to compute the middle index of the array. The number of times the array can be divided in half is proportional to the logarithm of the array size ($O(\log2 n)$ = $O(\log n)$).
    return merge(arr1=merge_sort(left), arr2=merge_sort(right))


if __name__ == "__main__":
    arr = [11, 64, 34, 25, 12, 22, 90]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
