clothes = [int(x) for x in input().split()]
capacity = int(input())

count = 1
available_capacity = capacity

while clothes:
    if clothes[-1] <= available_capacity:
        available_capacity -= clothes.pop()
    else:
        count += 1
        available_capacity = capacity

print(count)
