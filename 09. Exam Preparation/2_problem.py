def find_king(area, symbol):
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == symbol:
                return r, c


def in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


N = 8
board = []
for _ in range(N):
    board.append(input().split())

moves = [(-1, 1), (0, 1), (1, 1), (1, 0),
         (1, -1), (0, -1), (-1, -1), (-1, 0)]

result = []
r_k, c_k = find_king(board, 'K')

for move in moves:
    next_row = r_k + move[0]
    next_col = c_k + move[1]
    while in_range(next_row, next_col, N):
        if board[next_row][next_col] == 'Q':
            result.append([next_row, next_col])
            break
        next_row += move[0]
        next_col += move[1]

if result:
    [print(x) for x in result]
else:
    print('The king is safe!')
