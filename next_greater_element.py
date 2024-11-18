def find_nges(arr: list, verbose: bool = False) -> list:
    """
    e.g.,
    `arr`: `[3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]`
    1: 0 -> ok
    2: 1 -> x (index 1을 `stack`에 다시 넣습니다.)
    3: 2 -> x (index 2를 `stack`에 다시 넣습니다. index 3이 index 2보다 크지 않으므로 (index 3이 index 2보다 작거나 같으므로) index 1은 고려할 필요가 없습니다. 왜냐하면 index 3이 index 1보다 컸다면 NGE를 이미 찾은 것이고 반대라면 index 2도 index 1보다 컸을 것이므로 `stack`에 들어있지 않았을 것이기 때문입니다.
    4: 3 -> x (index 3을 `stack`에 다시 넣습니다.)
    5: 4 -> ok
    5: 3 -> x (index 3을 `stack`에 다시 넣습니다.)
    6: 5 -> ok
    6: 3 -> ok
    6: 2 -> ok
    6: 1 -> x (index 1을 `stack`에 다시 넣습니다.)
    ...
    `answer`: `[1, -1, 6, 6, 5, 6, 8, 8, 10, 10, -1]`
    """
    stack = [0]  # 아직 NGE를 찾지 못한 `arr`의 인덱스들.
    answer = [-1 for _ in range(len(arr))]
    for trg_idx in range(1, len(arr)):
        while stack:
            if verbose:
                print(f"{trg_idx}, {stack}")
            idx = stack.pop()
            if arr[trg_idx] > arr[idx]:
                if verbose:
                    print("ok")
                answer[idx] = trg_idx
            else:
                stack.append(idx)
                break
        stack.append(trg_idx)
    return answer


if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    print(find_nges(arr, verbose=True))
