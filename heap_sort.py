# References:
    # https://medium.com/@ishta.pal/heap-sort-explained-using-python-4f1466509521


def heapify(arr, root_idx, heap_size):
    """
    Heapify is the process of creating a heap data structure from a binary tree.
    Args:
        `heap_size`: This is the size of the heap, which tells the function how far the heap goes (i.e., how many elements are considered part of the heap). It is used to prevent accessing elements outside the bounds of the heap.
    """
    # by definition the leaves, i.e. nodes which are at the end will be satisfying the max heap property by definition, so we don’t want apply the heapify function on those leaves.
    largest = root_idx  # Initially, assume that the node at `index` is the largest.
    left = 2 * root_idx + 1
    right = 2 * root_idx + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root_idx:  # one of the children is larger than the parent.
        arr[largest], arr[root_idx] = arr[root_idx], arr[largest]
        heapify(arr, root_idx=largest, heap_size=heap_size)
    print(arr)


def heap_sort(arr):
    # Start from the last non-leaf node
    for root_idx in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, root_idx=root_idx, heap_size=len(arr))
    # [25, 45, 19, 66, 14, 1]
    # [25, 66, 19, 45, 14, 1]
    # [66, 25, 19, 45, 14, 1]
    # [66, 45, 19, 25, 14, 1]  Now the maximum element is at the root node.

    for idx in range(len(arr) -1, -1, -1):
        # So, we swap the root node with the leaf node at the end and thus we achieved to sort 1 element at the end of the array.
        arr[0], arr[idx] = arr[idx], arr[0]
        print(arr)
        heapify(arr, root_idx=0, heap_size=idx)


if __name__ == "__main__":
    # arr = [11, 64, 34, 25, 12, 22, 90]
    arr = [25, 45, 1, 66, 14, 19]
    # heapify(arr, heap_size=len(arr), root_idx=0)
    heap_sort(arr)
    # print(arr)
