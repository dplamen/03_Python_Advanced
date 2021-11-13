def is_valid(r, c, m):
    return 0 <= r < len(m) and 0 <= c < len(m[r])


rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
line = input()

while line != 'END':
    line = line.split()
    oper = line[0]
    row, col, value = [int(x) for x in line[1:]]
    if is_valid(row, col, matrix):
        if oper == 'Add':
            matrix[row][col] += value
        elif oper == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    line = input()

[print(f"{' '.join([str(x) for x in row])}") for row in matrix]

