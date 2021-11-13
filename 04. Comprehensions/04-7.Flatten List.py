matrix = [x.split() for x in input().split('|')][::-1]
print(f"{' ' .join([num for sublist in matrix for num in sublist])}")
