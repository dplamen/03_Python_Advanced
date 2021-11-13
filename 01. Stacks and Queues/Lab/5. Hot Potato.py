from collections import deque

names = deque(input().split())
n = int(input())

while len(names) > 1:
    names.rotate(1-n)
    print(f'Removed {names.popleft()}')

print(f'Last is {names.pop()}')

