n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(x) for x in input().split()])

prim_sum = 0
sec_sum = 0
for row in range(n):
    for col in range(n):
        if row == col:
            prim_sum += matrix[row][col]
        if row == n - 1 - col:
            sec_sum += matrix[row][col]

print(abs(prim_sum - sec_sum))

