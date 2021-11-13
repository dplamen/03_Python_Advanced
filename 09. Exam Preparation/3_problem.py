def best_list_pureness(numbers, k):
    best = 0
    rotations_count = 0
    for i in range(k+1):
        pureness = 0
        for idx in range(len(numbers)):
            pureness += numbers[idx] * idx
        if pureness > best:
            best = pureness
            rotations_count = i
        numbers = numbers[-1:] + numbers[0:-1]
    return f'Best pureness {best} after {rotations_count} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
