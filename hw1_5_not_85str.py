s = str(input("s = "))
first_mark = ['/', '*']
second_mark = ['+', '-']
mark = ['/', '*', '+', '-']
l = int(len(s))
for i in range(0, l):
    if s[i] in first_mark:
        num = int(s[i-1])
        div = int(s[i+1])
        ten = 10
        temp = s[i]
        del s[i]
        kn = 2
        while s[i-kn] not in mark:
            num += int(s[i-kn])*ten
            ten *= 10
            del s[i - kn]
            kn += 1
        kd = 2
        while s[i+kd] not in mark:
            div = div * 10 + int(s[i+kd])
            del s[i + kd]
            kd += 1
        if temp == '/':
            s[i-kn+1] = num/div
        else: s[i-kn+1] = num * div
for i in range(0, l):
    if s[i] in second_mark:
        temp = s[i]
        del s[i]
        kn = 1
        kd = 1
        num = int(s[i - 1])
        div = int(s[i + 1])
        ten = 10
        while s[i - kn] not in mark:
            num += int(s[i - kn]) * ten
            ten *= 10
            del s[i - kn]
            kn += 1
        kd = 2
        while s[i + kd] not in mark:
            div = div * 10 + int(s[i + kd])
            del s[i + kd]
            kd += 1
        if temp == '+': s[i-kn+1]=num+div
        else: s[i-kn+1]=num-div
print ('s = ',s)



