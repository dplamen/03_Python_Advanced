from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(y) for y in input().split()]

waste = 0
while cups:
    if bottles[-1] >= cups[0]:
        waste += bottles.pop() - cups.popleft()
    elif bottles[-1] < cups[0]:
        cups[0] -= bottles.pop()
    if not bottles:
        break

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f'Wasted litters of water: {waste}')


