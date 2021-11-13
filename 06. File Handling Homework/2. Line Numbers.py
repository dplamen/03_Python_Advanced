import string
letters = string.ascii_letters
punctuation = string.punctuation


def count_chars(criteria, lookup_range):
    count = 0
    for ch in lookup_range:
        if ch in criteria:
            count += 1
    return count


with open('text.txt', 'r') as f:
    lines = f.read().split('\n')

with open('output.txt', 'w') as out:
    output = []
    for i, line in enumerate(lines):
        count_letters = count_chars(letters, line)
        count_marks = count_chars(punctuation, line)
        output.append(f'Line {i}: {line} ({count_letters})({count_marks})')
    out.write('\n'.join(output))
