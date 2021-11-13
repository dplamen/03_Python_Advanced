n = int(input())
odd_set = set()
even_set = set()
for i in range(n):
    name = input()
    suma = 0
    for ch in name:
        suma += ord(ch)
    suma = suma // (i + 1)
    if suma % 2 == 0:
        even_set.add(suma)
    else:
        odd_set.add(suma)


if sum(odd_set) == sum(even_set):
    print(f"{', '.join([str(x) for x in odd_set.union(even_set)])}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join([str(x) for x in odd_set.difference(even_set)])}")
else:
    print(f"{', '.join([str(x) for x in odd_set.symmetric_difference(even_set)])}")
