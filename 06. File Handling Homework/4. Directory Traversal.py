import os

directory = input('Please provide a directory, for example - C:\\ : ')
directory = directory.replace('\\', '\\\\')
x = [f.name for f in os.scandir(directory) if f.is_file()]
files = {}
for file in x:
    extension = file.split('.')[-1]
    if extension not in files:
        files[extension] = []
    files[extension].append(file)

with open(os.path.join(os.environ['USERPROFILE'],'Desktop', 'report.txt'), 'w') as f:
    for k, v in sorted(files.items(), key=lambda a: (a[0], a[1])):
        f.write(f".{k}\n")
        f.write(''.join([f'- - - {x}\n' for x in v]))

