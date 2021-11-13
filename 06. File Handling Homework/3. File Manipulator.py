import os
import re
command = input()
while not command == 'End':
    operations = command.split('-')
    if operations[0] == 'Create':
        file = open(operations[1], 'w')
        file.close()
    elif operations[0] == 'Add':
        with open(operations[1], 'a') as file:
            file.write(operations[2]+'\n')
    elif operations[0] == 'Replace':
        if os.path.exists(operations[1]):
            with open(operations[1], 'r') as file:
                old_string = file.read()
            with open(operations[1], 'w') as file:
                file.write(re.sub(operations[2], operations[3], old_string))
        else:
            print('An error occurred')
    elif operations[0] == 'Delete':
        if os.path.exists(operations[1]):
            os.remove(operations[1])
        else:
            print('An error occurred')
    command = input()

