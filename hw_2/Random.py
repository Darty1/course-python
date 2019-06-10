import random as rand

n = rand.randint(1, 10)

k = input('guess, please: ')
while k != n:
    k = input('no, guess again, please: ')
else:
    print("you win, it's ", k)



