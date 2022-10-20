patch = 'file.txt'
data = open (patch, 'r')
for line in data:
    print(line, end = ' ')
data.close()