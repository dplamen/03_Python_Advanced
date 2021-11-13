from collections import deque


def is_in_range(dictionary):
    if all([value >= 3 for value in dictionary.values()]):
        return False
    return True


firework_effects = deque([int(x) for x in input().split(", ") if int(x) > 0])
explosive_power = deque([int(x) for x in input().split(", ") if int(x) > 0])

dict_fireworks = {"Palm": 0, "Willow": 0, "Crossette": 0}

while firework_effects and explosive_power and is_in_range(dict_fireworks):
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()
    current_sum = first_firework + last_explosive
    if current_sum % 15 == 0:
        dict_fireworks['Crossette'] += 1
    elif current_sum % 5 == 0:
        dict_fireworks['Willow'] += 1
    elif current_sum % 3 == 0:
        dict_fireworks['Palm'] += 1
    else:
        first_firework -= 1
        if first_firework > 0:
            firework_effects.append(first_firework)
        explosive_power.append(last_explosive)

if is_in_range(dict_fireworks):
    print(f"Sorry. You can't make the perfect firework show.")
else:
    print(f"Congrats! You made the perfect firework show!")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
for k, v in dict_fireworks.items():
    print(f"{k} Fireworks: {v}")
