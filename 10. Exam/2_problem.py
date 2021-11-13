def find_pos(area, symbol):
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == symbol:
                return [r, c]


def in_range(area, r, c):
    if 0 <= r < len(area) and 0 <= c < len(area[r]):
        return True
    return False


def count_pos(area, symbol):
    count = 0
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == symbol:
                count += 1
    return count


N = 5
matrix = []
for row in range(N):
    matrix.append(input().split())

n = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
targets_shoot = []
current_pos = find_pos(matrix, 'A')

for _ in range(n):
    line = input().split()
    new_row, new_col = current_pos
    if line[0] == 'move':
        new_row = current_pos[0] + directions[line[1]][0] * int(line[2])
        new_col = current_pos[1] + directions[line[1]][1] * int(line[2])
        if in_range(matrix, new_row, new_col):
            if matrix[new_row][new_col] == '.':
                current_pos = matrix[new_row][new_col]

    elif line[0] == 'shoot':
        step = 1
        while True:
            new_row = current_pos[0] + directions[line[1]][0] * step
            new_col = current_pos[1] + directions[line[1]][1] * step
            if in_range(matrix, new_row, new_col):
                if matrix[new_row][new_col] == 'x':
                    matrix[new_row][new_col] = '.'
                    targets_shoot.append([new_row, new_col])
                    break
            else:
                break
            if count_pos(matrix, 'x') == 0:
                break
            step += 1

    if count_pos(matrix, 'x') == 0:
        print(f"Training completed! All {len(targets_shoot)} targets hit.")
        break

if count_pos(matrix, 'x') > 0:
    print(f"Training not completed! {count_pos(matrix, 'x')} targets left.")

if targets_shoot:
    [print(x) for x in targets_shoot]