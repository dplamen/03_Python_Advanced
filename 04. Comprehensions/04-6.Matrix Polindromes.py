row, col = [int(x) for x in input().split()]
[print(f"{' '.join([chr(97 + r) + chr(97 + r + c) + chr(97 + r) for c in range(col)])}")
 for r in range(row)]
