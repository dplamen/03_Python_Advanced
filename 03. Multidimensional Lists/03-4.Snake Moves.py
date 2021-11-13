rows, columns = [int(x) for x in input().split()]
string = input()
matrix = []
i = 0

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        if row % 2 == 0:
            matrix[row].append(string[i])
        else:
            matrix[row].insert(0, string[i])
        i += 1
        if i == len(string):
            i = 0

for _ in range(rows):
    print(f"{''.join(matrix[_])}")

