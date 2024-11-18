"""
Using the middle element as a pivot divides the array into two very small sub-arrays, which leads to deeper recursion and many unnecessary comparisons. This increases the recursion depth and results in worse performance, especially as the array grows larger.
"""

# def quick_sort(arr: list) -> list:
#     if len(arr) <= 1:
#         return arr

#     pivot_idx = len(arr) // 2
#     pivot = arr[pivot_idx]
#     left = []
#     right = []
#     for idx in range(len(arr)):
#         if idx == pivot_idx:
#             continue

#         if arr[idx] <= pivot:
#             left.append(arr[idx])
#         else:
#             right.append(arr[idx])
#     return [*quick_sort(left), pivot, *quick_sort(right)]


def quick_sort(left_idx, right_idx):
    print(left_idx, right_idx)
    # print(left_idx, right_idx, arr[left_idx: right_idx + 1])
    ori_left_idx = left_idx
    ori_right_idx = right_idx
    if right_idx - left_idx <= 1:
        return

    pivot_idx = (left_idx + right_idx) // 2
    pivot = arr[pivot_idx]
    # We rearrange the array such that all elements smaller than the pivot are on its left and larger elements are on its right.
    while left_idx <= right_idx:
        while arr[left_idx] <= pivot:
            left_idx += 1  # 이 과정이 끝나면 `arr[left_idx]`는 `pivot`보다 큼.
        while arr[right_idx] > pivot:
            right_idx -= 1
        if left_idx <= right_idx:
            # print(left_idx, right_idx)
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
    # print((left_idx + right_idx) // 2, left_idx, right_idx)
    quick_sort(left_idx=ori_left_idx, right_idx=pivot_idx - 1)
    quick_sort(left_idx=pivot_idx, right_idx=ori_right_idx)


if __name__ == "__main__":
    arr = [11, 64, 34, 25, 12, 22, 90]
    # quick_sort(arr)

    quick_sort(left_idx=0, right_idx=len(arr) - 1)
    print(arr)
