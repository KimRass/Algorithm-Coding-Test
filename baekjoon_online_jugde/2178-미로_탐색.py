from collections import deque


def get_answer(N, M, arr):
    steps = dict()
    for row in range(N):
        for col in range(M):
            steps[(row, col)] = 0
    max_step = 0
    queue = deque([((0, 0), 1)])

    while queue:
        (cur_row, cur_col), cur_step = queue.popleft()
        if arr[cur_row][cur_col] == 1 and steps[(cur_row, cur_col)] == 0:
            steps[(cur_row, cur_col)] = cur_step
            if cur_step > max_step:
                max_step = cur_step
            if cur_row == N - 1 and cur_col == M - 1:
                return max_step
            for next_node in [
                    ((cur_row, cur_col)[0] - 1, (cur_row, cur_col)[1]),
                    ((cur_row, cur_col)[0] + 1, (cur_row, cur_col)[1]),
                    ((cur_row, cur_col)[0], (cur_row, cur_col)[1] - 1),
                    ((cur_row, cur_col)[0], (cur_row, cur_col)[1] + 1),
            ]:
                if 0 <= next_node[0] < N and 0 <= next_node[1] < M:
                    queue.append((next_node, cur_step + 1))
    return max_step


if __name__ == "__main__":
    # N = 4
    # M = 6
    # arr = [
    #     [1, 0, 1, 1, 1, 1],
    #     [1, 0, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 1, 1],
    #     [1, 1, 1, 0, 1, 1],
    # ] # 15
    # N = 4
    # M = 6
    # arr = [
    #     [1, 1, 0, 1, 1, 0],
    #     [1, 1, 0, 1, 1, 0],
    #     [1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 0, 1],
    # ] # 9
    # N = 2
    # M = 25
    # arr = [
    #     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    #     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    # ] # 38
    N, M = list(map(int, input().split()))
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input())))

    print(get_answer(N, M, arr))
