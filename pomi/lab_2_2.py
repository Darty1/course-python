import os
file_name = input("File name: ")
os.startfile('D:\study\python\lesson')
try:
    f = open(file_name+'.txt', 'r+')
except FileNotFoundError:
    print('File not found')
else:
    content = f.read().lower()
    content = content.replace(" ", '')
    content = content.replace("\n", '')
    if len(content) == 0:
        print('File is empty')
        exit()
    s = {}
    for i in content:
        s[i] = 0
    for i in content:
        s[i] += 1

    for i in s:
        print(i+' -> '+str(s[i]))