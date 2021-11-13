rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append(input().split())
command = input()
while command != 'END':
    is_valid = True
    parameters = command.split()
    if parameters[0] == 'swap' and len(parameters) == 5:
        coordinates = [int(x) for x in parameters[1:]]
        r1, c1, r2, c2 = [int(x) for x in coordinates]
        if 0 <= r1 < rows and 0 <= r2 < rows and \
                0 <= c1 < columns and 0 <= c2 < columns and \
                (r1 != r2 or c1 != c2):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in range(rows):
                print(f"{' '.join(matrix[row])}")
        else:
            is_valid = False
    else:
        is_valid = False
    if not is_valid:
        print('Invalid input!')
    command = input()
