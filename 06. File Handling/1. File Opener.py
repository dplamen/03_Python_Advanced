# try:
#     file = open('text.txt')
#     print('File found')
#     file.close()
# except FileNotFoundError:
#     print('File not found')

from os import path
if path.exists('text.txt'):
    print('File found')
    file = open('text.txt')
    file.close()
else:
    print('File not found')
