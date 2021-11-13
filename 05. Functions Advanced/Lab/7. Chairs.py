def combinations(n, names, current_names=[]):
    if len(current_names) == n:
        print(f"{', '.join(current_names)}")
        return
    for i in range(len(names)):
        current_names.append(names[i])
        combinations(n, names[i+1:], current_names)
        current_names.pop()


names = input().split(', ')
n = int(input())
combinations(n, names, current_names=[])

