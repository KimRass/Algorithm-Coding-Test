def bubble_sort(arr: list, verbose=False) -> list:
    """
    In-place Bubble sort
    """
    for leng in range(len(arr), 0, -1):
        # 한 번의 루프가 끝날 때마다, `leng` 만큼의 길이를 갖는 리스트에서 가장 큰 원소는 가장 오른쪽에 배치될 것이 보장됩니다.
        swapped = False
        for idx in range(leng - 1):
            if verbose:
                print(idx, idx + 1)
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
        if verbose:
            print(arr, swapped)
        if not swapped:
            break


if __name__ == "__main__":
    arr = [11, 64, 34, 25, 12, 22, 90]
    bubble_sort(arr)
    print(arr)
