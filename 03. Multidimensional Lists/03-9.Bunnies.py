import copy


def find_element(m, symbol):
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == symbol:
                return r, c


def bunnies_spread(m):
    out = copy.deepcopy(m)
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 'B':
                if c - 1 >= 0:
                    out[r][c - 1] = 'B'
                if c + 1 < len(m[0]):
                    out[r][c + 1] = 'B'
                if r - 1 >= 0:
                    out[r - 1][c] = 'B'
                if r + 1 < len(m):
                    out[r + 1][c] = 'B'
    return out


rows, columns = [int(x) for x in input().split()]
liar = []
for row in range(rows):
    liar.append(list(input()))
commands = list(input())
start_row, start_col = find_element(liar, 'P')
liar[start_row][start_col] = '.'
for command in commands:
    move = False
    if command == 'L' and start_col - 1 >= 0:
        start_col -= 1
        move = True
    if command == 'R' and start_col + 1 < len(liar[0]):
        start_col += 1
        move = True
    if command == 'U' and start_row - 1 >= 0:
        start_row -= 1
        move = True
    if command == 'D' and start_row + 1 < len(liar):
        start_row += 1
        move = True
    liar = bunnies_spread(liar)
    if move:
        if liar[start_row][start_col] == 'B':
            for row in range(rows):
                print(f"{''.join(liar[row])}")
            print(f'dead: {start_row} {start_col}')
            break
    else:
        for row in range(rows):
            print(f"{''.join(liar[row])}")
        print(f'won: {start_row} {start_col}')
        break








