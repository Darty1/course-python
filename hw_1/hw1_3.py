n = int(input("n = "))
s = []

for i in range(0, n):
    s.append(int(input('s = ')))

for i in range(0, n):
    if s[i] == 0:
        s.pop(i)
        s.insert(0, 0)


print (s)