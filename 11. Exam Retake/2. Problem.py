def find_pos(area, symbol):
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == symbol:
                return [r, c]


def in_range(area, r, c):
    if 0 <= r < len(area) and 0 <= c < len(area[r]):
        return True
    return False


n = int(input())
matrix = []
for row in range(n):
    matrix.append(input().split())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)}

current_pos = find_pos(matrix, 'A')
row, col = current_pos
tea_bags = 0
failed = False

command = input()
while command:
    matrix[row][col] = '*'
    row += directions[command][0]
    col += directions[command][1]
    if in_range(matrix, row, col):
        try:
            tea_bags += int(matrix[row][col])
            matrix[row][col] = '*'
            if tea_bags >= 10:
                break
        except ValueError:
            if matrix[row][col] == 'R':
                matrix[row][col] = '*'
                failed = True
                break
    else:
        failed = True
        break
    command = input()

if failed:
    print("Alice didn't make it to the tea party.")
if tea_bags >= 10:
    print("She did it! She went to the party.")

[print(' '.join(x)) for x in matrix]
