n = int(input())
s = []
for i in range(0, n):
    s.append(int(input()))
max1 = s[0]
max2 = 0
for i in range(0, n):
    if s[i] > max1:
        max1 = s[i]
    elif s[i] > max2 < max1:
        max2 = s[i]
print ("max1 = ", max1, "max2 = ", max2)