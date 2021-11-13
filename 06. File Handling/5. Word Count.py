import re
result = {}

with open('words.txt', 'r') as target:
    searched_words = target.read().lower().split()
with open('input.txt', 'r') as searched:
    checked_string = searched.read().lower()

pattern = r'[a-zA-Z]+'
checked_lst = re.findall(pattern, checked_string)
for word in searched_words:
    result[word] = checked_lst.count(word)

for k, v in sorted(result.items(), key=lambda x: -x[1]):
    print(f'{k} - {v}')


