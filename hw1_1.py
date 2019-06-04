s = str(input('input str: '))
l = len(s) - 1
i = 0
t = False
while i < l/2:
    if s[i] == s[l-i]:
        t = True
        i += 1
    else:
        t = False
        break
if t:
    print ('s is polindrom')
else:
    print('s is not polindrom')