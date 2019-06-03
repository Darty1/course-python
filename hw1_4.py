import math

n = int(input('n = '))
x = float(input('x = '))

count = 1
sum_cos = 1
for i in range(0, n-1):
    count *= (-1)*x*x/(i+1)/(i+2)
    sum_cos += count

print ('cos x = ', sum_cos)
print ('math cos x = ', math.cos(x))