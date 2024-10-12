import copy


class Backtracking(object):
    def __init__(self, trg_sum):
        self.out = []
        self.trg_sum = trg_sum

    # def backtrack(self, cur_cards, cur_sum, start_idx):
    #     for cur_idx in range(start_idx, len(cards)):
    #         if cur_sum >= self.trg_sum:
    #             cur_sum -= cur_cards.pop()
    #         if cur_sum < self.trg_sum:
    #             cur_cards.append(cards[cur_idx])
    #             cur_sum += cards[cur_idx]
    #         if cur_sum == self.trg_sum:
    #             self.out.append(copy.deepcopy(cur_cards))

    #         if cur_idx == len(cards) - 1:
    #             if len(cur_cards) >= 2:
    #                 self.backtrack(
    #                     cur_cards=cur_cards[: -2],
    #                     cur_sum=cur_sum - cur_cards[-1] - cur_cards[-2],
    #                     start_idx=cards.index(cur_cards[-2]) + 1,
    #                 )
    #             else:
    #                 break
    #     return self.out
    def backtrack(self, cur_cards, start_idx, cur_sum):
        if cur_sum == self.trg_sum:
            self.out.append(copy.deepcopy(cur_cards))
        elif cur_sum < self.trg_sum:
            for cur_idx in range(start_idx, len(cards)):
                cur_cards.append(cards[cur_idx])
                self.backtrack(
                    cur_cards=cur_cards,
                    start_idx=cur_idx + 1,
                    cur_sum=cur_sum + cards[cur_idx],
                )
                cur_cards.pop()
        return self.out

    def __call__(self):
        return self.backtrack(cur_cards=[], cur_sum=0, start_idx=0)


if __name__ == "__main__":
    coin = 4
    cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]

    backtracking = Backtracking(trg_sum=max(cards) + 1)
    out = backtracking()
    print(*out, sep="\n")
    # []
    # [3]
    # [3, 6]
    # [3, 6, 7]
    # [3, 6, 2]
    # [3, 6, 2, 1]
    # [3, 6, 2, 1, 10]
    # [3, 6, 2, 1, 5]
    # [3, 6, 2, 1, 9]
    # [3, 6, 2, 1, 8]
    # [3, 6, 2, 1, 12]
    # [3, 6, 2, 1, 11]
    # [3, 6, 2, 1, 4] 끝
    # [3, 6, 2]
    # [3, 6, 2, 10]
    # [3, 6, 2, 5]
    # [3, 6, 2, 9]
    # [3, 6, 2, 8]
    # [3, 6, 2, 12]
    # [3, 6, 2, 11]
    # [3, 6, 2, 4] 끝
    # [3, 6]
    # [3, 6, 1]
    # [3, 6, 1, 10]
    # [3, 6, 1, 5]
    # [3, 6, 1, 9]
    # [3, 6, 1, 8]
    # [3, 6, 1, 12]
    # [3, 6, 1, 11]
    # [3, 6, 1, 4] 끝
    # [3, 6]
    # [3, 6, 10]
    # [3, 6, 5]
    # [3, 6, 9]
    # [3, 6, 8]
    # [3, 6, 12]
    # [3, 6, 11]
    # [3, 6, 4] 통과 끝
    # [3]
    # [3, 7]
    # [3, 7, 2]
    # [3, 7, 2, 1] 통과
    # [3, 7, 2, 10]
    # [3, 7, 2, 5]
    # [3, 7, 2, 9]
    # [3, 7, 2, 8]
    # [3, 7, 2, 12]
    # [3, 7, 2, 11]
    # [3, 7, 2, 4] 끝
    # [3, 7]
    # [3, 7, 1]
    # [3, 7, 1, 10]
    # [3, 7, 1, 5]
    # [3, 7, 1, 9]
    # [3, 7, 1, 8]
    # [3, 7, 1, 12]
    # [3, 7, 1, 11]
    # [3, 7, 1, 4] 끝
