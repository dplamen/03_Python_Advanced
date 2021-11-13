parentheses = input()

stack = []
balanced = True
for ch in parentheses:
    if ch in '([{':
        stack.append(ch)
    elif stack and (stack.pop() + ch) in ('{}', '[]', '()'):
        continue
    else:
        balanced = False
        break
if balanced:
    print('YES')
else:
    print('NO')
