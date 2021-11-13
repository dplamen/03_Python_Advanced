n = int(input())
stack = []
stack_reverse = []
for i in range(n):
    line = input().split()
    if line[0] == '1':
        stack.append(int(line[1]))
    elif line[0] == '2' and stack:
        stack.pop()
    elif line[0] == '3' and stack:
        print(max(stack))
    elif line[0] == '4' and stack:
        print(min(stack))

while stack:
    stack_reverse.append(str(stack.pop()))

print(', '.join(stack_reverse))
