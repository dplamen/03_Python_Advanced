import re

with open('text.txt', 'r') as f:
    lines = f.read().split('\n')

for idx, line in enumerate(lines):
    if idx % 2 == 0:
        words = re.sub(r'[-,.!?]', '@', line).split()[::-1]
        print(' '.join(words))

