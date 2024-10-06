from collections import deque


class Solution(object):
    def __init__(self, N, M, arr):
        self.N = N
        self.M = M
        self.arr = arr
        self.steps = dict()
        for row in range(self.N):
            for col in range(self.M):
                self.steps[(row, col)] = 0
        self.max_step = 0
        self.queue = deque([((0, 0), 1)])

    def bfs(self):
        while self.queue:
            (cur_row, cur_col), cur_step = self.queue.popleft()
            if arr[cur_row][cur_col] == 1 and self.steps[(cur_row, cur_col)] == 0:
                self.steps[(cur_row, cur_col)] = cur_step
                if cur_step > self.max_step:
                    self.max_step = cur_step
                if cur_row == self.N - 1 and cur_col == self.M - 1:
                    return self.max_step
                for next_node in [
                        ((cur_row, cur_col)[0] - 1, (cur_row, cur_col)[1]),
                        ((cur_row, cur_col)[0] + 1, (cur_row, cur_col)[1]),
                        ((cur_row, cur_col)[0], (cur_row, cur_col)[1] - 1),
                        ((cur_row, cur_col)[0], (cur_row, cur_col)[1] + 1),
                ]:
                    if 0 <= next_node[0] < N and 0 <= next_node[1] < M:
                        self.queue.append((next_node, cur_step + 1))
        return self.max_step


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

    solution = Solution(N, M, arr)
    print(solution.bfs())
