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


def input_step(x1, y1):
    x1 = int(input('input x: '))
    y1 = int(input('input y: '))


def make_turn(L, xx, yy, player):
    fool = '|  '
    print(player, ' - move ')
    input_step(xx, yy)
    if 1 > xx > 3 or 1 > yy > 3:
        print('bad, input again')
        input_step(xx, yy)
    elif L[xx-1][yy-1] == fool:
        L[xx-1][yy-1] = player
        temp = False
    elif L[xx-1][yy-1] != fool:
        temp = check_win(L, xx, yy, player)
        check_draw(L)
    return temp

def check_win(L, i, j, play):
    while True:
        k = 1
        if k > 2:
            print(play,' - win')
            break
            return True
        if L[i-1+k][j-1] == play:
            k += 1
            continue
        elif L[i-1][j-1+k] == play:
            k += 1
            continue
        elif L[i-1+k][j-1+k] == play:
            k += 1
            continue
    return False
def check_draw(L):
    print(':(')
