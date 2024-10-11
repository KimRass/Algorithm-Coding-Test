# 1 12 7 11 9 6 10 11 1* 12 7 11**
# 2 막다른
# 3 5 3* 8 3**
# 4 8 3 5 3* 8* 3**
# 5 3 8 3* 5* 3**
# 6 10 11 1 12 7 11* 9 6 10 11**

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

from collections import defaultdict, deque

outs = defaultdict(list)
ins = defaultdict(list)
cnts = defaultdict(int)
for start, end in edges:
    outs[start].append(end)
    ins[end].append(start)
    cnts[start] += 1
    cnts[end] -= 1
gen = sorted(cnts.items(), key=lambda x: x[1])[-1][0]
total_num = len(outs[gen])
outs[gen] = []
ins = {k: [i for i in v if i != gen] for k, v in ins.items()}
outs
ins

out_is2 = {k: sorted(v) for k, v in outs.items() if len(v) == 2}
in_is2 = {k: sorted(v) for k, v in ins.items() if len(v) == 2}
out_is2
in_is2

num_donuts = 0
num_eights = 0
# num_sticks = 0
for i, j in out_is2.items():
    if j == in_is2[i]:
        num_donuts += 1
    else:
        num_eights += 1
num_donuts, num_eights, total_num - num_donuts - num_eights


steps = {k: len(v) for k, v in outs.items()}
def dfs(start_node):
    stack = [start_node]
    while stack:
        cur_node = stack.pop()
        print(cur_node, end=" ")
        # steps[cur_node] += 1
        steps[cur_node] -= 1
        for next_node in outs[cur_node]:
            if steps[next_node] > 0:
                stack.append(next_node)

for start_node in outs[gen]:
    print(start_node)
    dfs(start_node)
