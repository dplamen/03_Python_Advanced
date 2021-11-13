# import os
# if os.path.exists('python'):
#     os.remove('python.txt')
# else:
#     print('File already deleted!')

import os
try:
    os.remove('python.txt')
except FileNotFoundError:
    print('File already deleted!')