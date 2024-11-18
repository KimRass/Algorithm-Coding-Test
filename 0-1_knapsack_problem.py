# References: https://gsmesie692.tistory.com/113
mem = dict()
# largest_value(idx_bef, max_w): Index `idx_bef` 전까지의 Items를 가지고 무게 `max_w` 이하로 만들 수 있는 최대 Value.
def largest_value(idx_bef, max_w):
    if (idx_bef, max_w) not in mem:
        if idx_bef == 0:
            if items[0][0] <= max_w:
                mem[(idx_bef, max_w)] = items[0][1]
            else:
                mem[(idx_bef, max_w)] = 0
        else:
            mem[(idx_bef, max_w)] = max(largest_value(idx_bef - 1, max_w - items[idx_bef][0]) + items[idx_bef][1], largest_value(idx_bef - 1, max_w)) if items[idx_bef][0] <= max_w else largest_value(idx_bef - 1, max_w)
    return mem[(idx_bef, max_w)]
