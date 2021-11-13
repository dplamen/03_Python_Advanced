from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value = int(input())

opened_flg = False
while locks:
    bullets_shot = 0
    while bullets:
        if bullets.pop() > locks[0]:
            print('Ping!')
        else:
            print('Bang!')
            locks.popleft()
        bullets_shot += 1
        if bullets_shot % barrel_size == 0:
            if bullets:
                print('Reloading!')
        if len(locks) == 0:
            opened_flg = True
            break
    if not bullets:
        break
if locks and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
if not locks:
    print(f'{len(bullets)} bullets left. Earned ${value - bullet_price * bullets_shot}')





