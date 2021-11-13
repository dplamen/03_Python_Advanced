def conflict_matrix(m):
    out_m = []
    for r in range(len(m)):
        out_m.append([])
        for c in range(len(m)):
            out_m[r].append(0)
            if m[r][c] == 'K':
                if r - 1 >= 0 and c - 2 >= 0 and m[r-1][c-2] == 'K':
                    out_m[r][c] += 1
                if r - 2 >= 0 and c - 1 >= 0 and m[r-2][c-1] == 'K':
                    out_m[r][c] += 1
                if r - 2 >= 0 and c + 1 < len(m) and m[r - 2][c + 1] == 'K':
                    out_m[r][c] += 1
                if r - 1 >= 0 and c + 2 < len(m) and m[r - 1][c + 2] == 'K':
                    out_m[r][c] += 1
                if r + 1 < len(m) and c + 2 < len(m) and m[r + 1][c + 2] == 'K':
                    out_m[r][c] += 1
                if r + 2 < len(m) and c + 1 < len(m) and m[r + 2][c + 1] == 'K':
                    out_m[r][c] += 1
                if r + 2 < len(m) and c - 1 >= 0 and m[r + 2][c - 1] == 'K':
                    out_m[r][c] += 1
                if r + 1 < len(m) and c - 2 >= 0 and m[r + 1][c - 2] == 'K':
                    out_m[r][c] += 1
    return out_m


def find_max(m):
    maximum = - 10000000
    max_col = 0
    max_row = 0
    for r in range(len(m)):
        for c in range(len(m)):
            if m[r][c] > maximum:
                maximum = m[r][c]
                max_row = r
                max_col = c
    return max_row, max_col


def remove_knight(m, r, c):
    if r - 1 >= 0 and c - 2 >= 0 and m[r - 1][c - 2] > 0:
        m[r][c] -= 1
        m[r - 1][c - 2] -= 1
    if r - 2 >= 0 and c - 1 >= 0 and m[r - 2][c - 1] > 0:
        m[r][c] -= 1
        m[r - 2][c - 1] -= 1
    if r - 2 >= 0 and c + 1 < len(m) and m[r - 2][c + 1] > 0:
        m[r][c] -= 1
        m[r - 2][c + 1] -= 1
    if r - 1 >= 0 and c + 2 < len(m) and m[r - 1][c + 2] > 0:
        m[r][c] -= 1
        m[r - 1][c + 2] -= 1
    if r + 1 < len(m) and c + 2 < len(m) and m[r + 1][c + 2] > 0:
        m[r][c] -= 1
        m[r + 1][c + 2] -= 1
    if r + 2 < len(m) and c + 1 < len(m) and m[r + 2][c + 1] > 0:
        m[r][c] -= 1
        m[r + 2][c + 1] -= 1
    if r + 2 < len(m) and c - 1 >= 0 and m[r + 2][c - 1] > 0:
        m[r][c] -= 1
        m[r + 2][c - 1] -= 1
    if r + 1 < len(m) and c - 2 >= 0 and m[r + 1][c - 2] > 0:
        m[r][c] -= 1
        m[r + 1][c - 2] -= 1
    return m


n = int(input())
board = []
for row in range(n):
    board.append(list(input()))

count = 0
board = conflict_matrix(board)

while find_max(board) != (0, 0):
    board = remove_knight(board, find_max(board)[0], find_max(board)[1])
    count += 1

print(count)
