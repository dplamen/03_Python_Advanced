file = open('python.txt', 'a')
lines = ["\n", "Write ", "in ", "file"]
file.writelines(lines)
file.close()
