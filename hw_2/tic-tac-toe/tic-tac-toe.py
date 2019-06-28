def print_grid(Ll):
    step = '+---+---+---+'
    for i in range(0, 3):
        if i != 0:
            print('|')
        print(step)
        for j in Ll[i]:
            print j,
    print('|')
    print(step)

def make_turn(L, xx, yy, player):
    fool = '|  '
    print(player, ' - move ')
    xx = int(input('input x: '))
    yy = int(input('input y: '))
    if 1 > xx > 3 or 1 > yy > 3:
        print('bad, input again')
        xx = int(input('input x: '))
        yy = int(input('input y: '))
    elif L[xx - 1][yy - 1] == fool:
        L[xx - 1][yy - 1] = player
        print('check')
        temp = check_win(L, xx, yy, player)
        if temp == False:
            print('check draw')
            temp = check_draw(L)
    elif L[xx - 1][yy - 1] != fool:
        print('bad, input again')
        temp = make_turn(L, xx, yy, player)
    return temp


def check_win(L, i, j, play):
    print('check win')
    p = False
    for s in range(0, 3):
        if L[i - 1][s] != play:
            p = False
            break
        if s == 2:
            print(play, ' - win')
            p = True
            break
    if p == False:
        for s in range(0, 3):
            if L[s][j - 1] != play:
                p = False
                break
            if s == 2:
                print(play, ' - win')
                p = True
                break
    if p == False:
        for s in range(0, 3):
            if L[s][s] != play:
                p = False
                break
            if s == 2:
                print(play, ' - win')
                p = True
                break
    k = 2
    if p == False:
        for s in range(0, 3):
            if L[s][k] != play:
                p = False
                break
            k -= 1
            if s == 2:
                print(play, ' - win')
                p = True
                break

    return p


def check_draw(L):
    r = 0
    ll = 0
    tr = True
    while tr:
        if r > 2:
            ll += 1
            r = 0
            if ll > 2:
                tr = True
                print ('its draw')
                break
        elif ll > 2:
            tr = False
            return False
            break
        if L[r][ll] == X or L[r][ll] == O:
            r += 1
        else:
            tr = False
            break
    return tr



fool = '|  '
a = 0
b = 0
p = ' '
t = True
check = True
mas = [[fool, fool, fool], [fool, fool, fool], [fool, fool, fool]]
print_grid(mas)

X = '| X'  # type: str
O = '| O'

turn = int(input('X - 1 or O - 0 first? '))
if turn == 1:
    turn = X
else:
    turn = O

while t:
    check = make_turn(mas, a, b, turn)
    print_grid(mas)
    if check:
        t = False
    if turn == O:
        turn = X
    else:
        turn = O
