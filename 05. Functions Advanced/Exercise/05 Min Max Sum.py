numbers = [int(x) for x in input().split()]
neg = sum(filter(lambda a: True if a < 0 else False, numbers))
pos = sum(filter(lambda a: True if a >= 0 else False, numbers))
print(neg)
print(pos)
print("The positives are stronger than the negatives") if pos > abs(neg) \
    else print("The negatives are stronger than the positives")
