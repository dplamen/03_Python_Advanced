# from collections import deque
# jobs = deque([int(x) for x in input().split(', ')])
# index = int(input())
#
# cycles_count = 0
# jobs.rotate(-1-index)
# for idx in range(len(jobs)):
#     if jobs[idx] <= jobs[-1]:
#         cycles_count += jobs[idx]
#
# print(cycles_count)
from collections import deque

jobs = [int(x) for x in input().split(', ')]
jobs = deque(sorted(enumerate(jobs), key=lambda x: (x[1], x[0])))
index_target = int(input())

cycles_count = 0
while jobs:
    index, value = jobs.popleft()
    cycles_count += value
    if index == index_target:
        print(cycles_count)
        break





