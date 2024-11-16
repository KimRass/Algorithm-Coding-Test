from collections import defaultdict


def solution(friends, gifts):
    friends.sort()

    give_and_takes = dict()
    indices = defaultdict(int)
    for i in range(len(friends)):
        for friend2 in friends[i:]:
            friend1 = friends[i]
            if friend1 != friend2:
                give_and_takes[(friend1, friend2)] = 0

    for gift in gifts:
        friend1, friend2 = gift.split()
        if (friend1, friend2) in give_and_takes:
            give_and_takes[(friend1, friend2)] += 1
        else:
            give_and_takes[(friend2, friend1)] -= 1
        indices[friend1] += 1
        indices[friend2] -= 1

    answer = defaultdict(int)
    for (friend1, friend2), num in give_and_takes.items():
        if num > 0:
            answer[friend1] += 1
        elif num < 0:
            answer[friend2] += 1
        elif indices[friend1] > indices[friend2]:
            answer[friend1] += 1
        elif indices[friend1] < indices[friend2]:
            answer[friend2] += 1
    if answer:
        return max(answer.values())
    else:
        return 0


if __name__ == "__main__":
    # friends = ["muzi", "ryan", "frodo", "neo"]
    # gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    friends = ["a", "b", "c"]
    gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
    solution(friends, gifts)
