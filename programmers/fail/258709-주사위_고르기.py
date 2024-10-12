import numpy as np

from itertools import combinations


def solution(dice):
    def add_dice(x, y):
        return (x[..., None] + y[None, ...]).reshape(-1,)

    def subtract_dice(x, y):
        return x[..., None] - y[None, ...]

    def recursive_add_dice(indices):
        out = dice[indices[0]]
        for j in indices[1:]:
            out = add_dice(out, dice[j])
        return out

    def get_indices2(indices1):
        return tuple([k for k in range(len(dice)) if k not in indices1])

    dice = np.array(dice)
    max_wins = 0
    wins_dict = dict()
    for indices1 in combinations(range(len(dice)), len(dice)//2):
        indices2 = get_indices2(indices1)
        if (indices2, indices1) in wins_dict:
            continue

        sum1 = recursive_add_dice(indices1)
        sum2 = recursive_add_dice(indices2)
        diff = subtract_dice(sum1, sum2)
        wins1 = np.sum(diff > 0)
        wins2 = np.sum(diff < 0)
        wins_dict[(indices1, indices2)] = (wins1, wins2)
        wins_dict[(indices2, indices1)] = (wins2, wins1)

        if wins1 > max_wins:
            max_wins = wins1
            best_indices = indices1
        if wins2 > max_wins:
            max_wins = wins2
            best_indices = indices2
    return [i + 1 for i in best_indices]


if __name__ == "__main__":
    dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]] # `[1, 4]`
    # dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]] # `[2]`
    # dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]] # `[1, 3]`

    solution(dice)
