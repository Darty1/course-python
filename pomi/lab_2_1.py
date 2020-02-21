file_name = input("File name: ")
try:
    f = open(file_name+'.txt', 'r+')
except FileNotFoundError:
    print('File not found')
else:
    content = f.read()
    if len(content) == 0:
        print('File is empty')
        exit()
    elif len(content) % 3 != 0:
        print('Wrong input')
        exit()
    content = content.split()
    students = {}
    for i in range(0, len(content), 3):
        students[content[i] + ' ' + content[i + 1]] = 0
    for i in range(2, len(content), 3):
        students[content[i - 2] + ' ' + content[i - 1]] += float(content[i])
    l = list(students.items())
    l.sort(key=lambda i: i[1])
    for i in l:
        print(i[0] + " "+str(i[1]))



