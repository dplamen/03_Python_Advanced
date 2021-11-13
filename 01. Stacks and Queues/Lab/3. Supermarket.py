from collections import deque

queue = deque()
line = input()
while line != 'End':
    if line != 'Paid':
        queue.append(line)
    else:
        while queue:
            print(queue.popleft())
    line = input()

print(f'{len(queue)} people remaining.')
