from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])

if orders:
    print(max(orders))

while orders:
    if orders[0] <= quantity:
        quantity -= orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")
