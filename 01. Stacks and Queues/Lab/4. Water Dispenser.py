from collections import deque

quantity = int(input())
command = input()
queue = deque()
while command != 'Start':
    queue.append(command)
    command = input()
command = input()
while command != 'End':
    if command.split()[0] == 'refill':
        quantity += int(command.split()[1])
    else:
        if int(command) <= quantity:
            print(f'{queue.popleft()} got water')
            quantity -= int(command)
        else:
            print(f'{queue.popleft()}  must wait')
    command = input()

print(f'{quantity} liters left.')
