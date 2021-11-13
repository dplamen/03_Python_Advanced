heroes_dict = {hero: {} for hero in input().split(', ')}
command = input()

while command != 'End':
    name, item, cost = command.split('-')
    if item not in heroes_dict[name]:
        heroes_dict[name][item] = int(cost)
    command = input()

{print(f'{k} -> Items: {len(v)}, Cost: {sum(v.values())}') for (k, v) in heroes_dict.items()}
