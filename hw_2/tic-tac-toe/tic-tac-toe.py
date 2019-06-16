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
    elif L[xx - 1][yy - 1] != fool:
        print('bad, input again')
        xx = int(input('input x: '))
        yy = int(input('input y: '))
        check_draw(L)
    return temp


def check_win(L, i, j, play):
    while True:
        k = 1
        if k > 2:
            print(play, ' - win')
            break
            return True
        if L[i - 1 + k][j - 1] == play:
            k += 1
            continue
        elif L[i - 1][j - 1 + k] == play:
            k += 1
            continue
        elif L[i - 1 + k][j - 1 + k] == play:
            k += 1
            continue
        else:
            break
    return False


def check_draw(L):
    print(':(')


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
        break
    if turn == O:
        turn = X
    else:
        turn = O
