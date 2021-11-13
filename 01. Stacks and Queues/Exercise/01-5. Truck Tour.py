from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    petrol, distance = [int(x) for x in input().split()]
    pumps.append([petrol, distance])

for i in range(n):
    fuel_tank = 0
    count = 0
    for pump in pumps:
        fuel, distance_to_next = pump[0], pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        else:
            fuel_tank -= distance_to_next
        count += 1
    if count == n:
        print(i)
        break
    pumps.rotate(-1)




