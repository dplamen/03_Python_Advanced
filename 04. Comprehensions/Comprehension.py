start_num = int(input())
end_num = int(input())

print([num
       for num in range(start_num, end_num + 1)
       if [div for div in range(2, 11) if num % div == 0]
       ])

