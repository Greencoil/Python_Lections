colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) #разделителей не будет
data.write('\nLINE 121\n')
data.write('LINE 131\n')
data.close()


