from collections import deque


def check_list(lst):
    if len(lst) < 1 or all(lst) < 0:
        return False
    return True


chocolate = [int(x) for x in input().split(', ')]
cup_milk = deque([int(x) for x in input().split(', ')])

shake_count = 0

while check_list(chocolate) and check_list(cup_milk) and shake_count < 5:
    choco = chocolate.pop()
    if choco <= 0:
        continue
    milk = cup_milk.popleft()
    if milk <= 0:
        chocolate.append(choco)
        continue
    if choco == milk:
        shake_count += 1
    else:
        cup_milk.append(milk)
        chocolate.append(choco - 5)
        if chocolate[-1] <= 0:
            chocolate.pop()

if shake_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print('Chocolate: empty')

if cup_milk:
    print(f"Milk: {', '.join([str(x) for x in cup_milk])}")
else:
    print('Milk: empty')




