def dfs(N):
    stack = [([], set(), set(), set())]
    cnt = 0
    while stack:
        cols, same_cols, diags, anti_diags = stack.pop()
        next_row = len(cols)
        if next_row == N:
            cnt += 1
        for next_col in range(N):
            if (
                next_col not in same_cols
                and next_col - next_row not in diags
                and next_col + next_row not in anti_diags
            ):
                stack.append(
                    (
                        cols + [next_col],
                        same_cols | {next_col},
                        diags | {next_col - next_row},
                        anti_diags | {next_col + next_row},
                    )
                )
    return cnt


if __name__ == "__main__":
    N = 4
    print(dfs(N))
