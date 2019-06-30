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

# можно было написать:
# t = True
# for i in range(l // 2):
#     if s[i] != s[l - i]:
#         t = False
#         break
# результат тот же, но выглядит куда проще

if t:
    print ('s is palindrom')
else:
    print('s is not palindrom')