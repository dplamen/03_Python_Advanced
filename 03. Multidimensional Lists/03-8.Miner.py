def find_element(m, symbol):
    for r in range(len(m)):
        for c in range(len(m)):
            if m[r][c] == symbol:
                return r, c


def count_element(m, symbol):
    count = 0
    for r in range(len(m)):
        for c in range(len(m)):
            if m[r][c] == symbol:
                count += 1
    return count


n = int(input())
commands = input().split()
matrix = []
for row in range(n):
    matrix.append(input().split())

coal = 0
f = True
start_row, start_col = find_element(matrix, 's')

for command in commands:
    if command == 'left' and start_col - 1 >= 0:
        start_col -= 1
    elif command == 'right' and start_col + 1 < n:
        start_col += 1
    elif command == 'up' and start_row - 1 >= 0:
        start_row -= 1
    elif command == 'down' and start_row + 1 < n:
        start_row += 1

    if matrix[start_row][start_col] == 'c':
        coal += 1
        matrix[start_row][start_col] = '*'
        if count_element(matrix, 'c') == 0:
            print(f'You collected all coals! ({start_row}, {start_col})')
            f = False
            break

    elif matrix[start_row][start_col] == 'e':
        print(f'Game over! ({start_row}, {start_col})')
        f = False
        break
if f:
    print(f"{count_element(matrix, 'c')} coals left. ({start_row}, {start_col})")






