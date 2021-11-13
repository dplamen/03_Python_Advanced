n = int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]

first_diag = [matrix[r][c] for r in range(n) for c in range(n) if r == c]
second_diag = [matrix[r][c] for r in range(n) for c in range(n) if r == n - 1 - c]

print(f"First diagonal: {', '.join([str(x) for x in first_diag])}. Sum: {sum(first_diag)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diag])}. Sum: {sum(second_diag)}")
