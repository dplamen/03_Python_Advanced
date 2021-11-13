def odd_even(command, nums):
    if command == 'Odd':
        return sum([x for x in nums if x % 2 != 0]) * len(nums)
    elif command == 'Even':
        return sum([x for x in nums if x % 2 == 0]) * len(nums)


print(odd_even(input(), [int(x) for x in input().split()]))
