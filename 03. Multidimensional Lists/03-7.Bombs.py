def explosion(m, r, c):
    if m[r][c] > 0:
        if r - 1 >= 0 and c - 1 >= 0 and m[r - 1][c - 1] > 0:
            m[r - 1][c - 1] -= m[r][c]
        if r - 1 >= 0 and m[r - 1][c] > 0:
            m[r - 1][c] -= m[r][c]
        if r - 1 >= 0 and c + 1 < len(m) and m[r - 1][c + 1] > 0:
            m[r - 1][c + 1] -= m[r][c]
        if c - 1 >= 0 and m[r][c - 1] > 0:
            m[r][c - 1] -= m[r][c]
        if c + 1 < len(m) and m[r][c + 1] > 0:
            m[r][c + 1] -= m[r][c]
        if r + 1 < len(m) and c - 1 >= 0 and m[r + 1][c - 1] > 0:
            m[r + 1][c - 1] -= m[r][c]
        if r + 1 < len(m) and m[r + 1][c] > 0:
            m[r + 1][c] -= m[r][c]
        if r + 1 < len(m) and c + 1 < len(m) and m[r + 1][c + 1] > 0:
            m[r + 1][c + 1] -= m[r][c]
        m[r][c] = 0
    return m


n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(x) for x in input().split()])

explosions = input().split()
for i in range(len(explosions)):
    row, column = [int(x) for x in explosions[i].split(',')]
    matrix = explosion(matrix, row, column)

count_alive = 0
sum_alive = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            count_alive += 1
            sum_alive += matrix[r][c]

print(f'Alive cells: {count_alive}')
print(f'Sum: {sum_alive}')
for row in range(n):
    print(f"{' '.join([str(x) for x in matrix[row]])}")
