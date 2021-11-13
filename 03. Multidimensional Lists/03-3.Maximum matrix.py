rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])
max_sum = 0
max_matrix = []
for row in range(rows-2):
    for col in range(columns-2):
        sum_next = 0
        sub_matrix = []
        for sub_row in range(3):
            sub_matrix.append([])
            for sub_col in range(3):
                sum_next += matrix[row+sub_row][col+sub_col]
                sub_matrix[sub_row].append(str(matrix[row+sub_row][col+sub_col]))
        if sum_next >= max_sum:
            max_sum = sum_next
            max_matrix = sub_matrix
print(f'Sum = {max_sum}')
for row in range(3):
    print(f"{' '.join(max_matrix[row])}")