import random

a = "Hello"

def print_grid(Ll):
    step = '+---+---+---+'
    a = 0
    b = 3
    print(step)
    for i in range(3):
        for j in range(a, b):
            print(Ll[j], end=' ')
        print('|')
        a += 3
        b += 3
        print(step)


def make_turn(L, player):
    X = '| X'
    O = '| O'
    x = int(input('Enter your move: '))
    while 0 >= x or x > 9:
        print('bad, input again')
        x = int(input('Enter your move: '))
    if L[x-1] not in [X, O]:
        L[x-1] = player
        temp = check_win(L, player)
        if temp is False:
            temp = check_draw(L)
    else:
        print('bad, input again')
        temp = make_turn(L, player)
    # print_grid(L)
    return temp


def comp_turn(L):
    t = random.randrange(0, 9)
    while L[t] in ['| O', '| X']:
        t = int(random.random()*9)
    L[t] = '| X'
    print("Comp turn:")
    temp = check_win(L, '| X')
    if temp is False:
        temp = check_draw(L)
    return temp


def check_win(L, play):
    p = False
    print_grid(L)
    for row in range(3):
        if L[row] == play:
            p = True
            for col in [row+3, row+6]:
                if L[col] != play:
                    p = False
                    break
            if p is True:
                if play == '| O':
                    print('You won!')
                else:
                    print('Comp won!')
                return p
    for row in range(0, 7, 3):
        if L[row] == play:
            p = True
            for col in range(row, row+3):
                if L[col] != play:
                    p = False
                    break
            if p is True:
                if play == '| O':
                    print('You won!')
                else:
                    print('Comp won!')
                return p

    if p is False and play == '| X':
        for s in [0, 4, 8]:
            if L[s] != '| X':
                p = False
                break
            elif s == 8:
                print('Comp won!')
                p = True
                break
    if p is False and play == '| X':
        for s in [2, 4, 6]:
            if L[s] != '| X':
                p = False
                break
            elif s == 6:
                print('Comp won!')
                p = True
                break
    return p


def check_draw(L):
    row = 0
    tr = False
    for l in L:
        if l in ['| X', '| O']:
            row += 1
        else:
            break
            tr = False
    if row == 9:
        tr = True
        print('Its Draw!')
    return tr
