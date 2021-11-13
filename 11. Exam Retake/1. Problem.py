from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0
ops = {"+": (lambda x, y: x+y),
       "-": (lambda x, y: x-y),
       "*": (lambda x, y: x*y),
       "/": (lambda x, y: x/y)}


while bees and nectar and symbols:
    if nectar[-1] >= bees[0]:
        try:
            honey_made += abs(ops[symbols.popleft()](bees.popleft(), nectar.pop()))
        except ZeroDivisionError:
            continue
    else:
        nectar.pop()
        continue

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")





