import tictacmoduls as ttm


fool = '|  '
a = 0
b = 0
p = ' '
t = True
check = True
mas = [[fool, fool, fool], [fool, fool, fool], [fool, fool, fool]]
ttm.print_grid(mas)

X = '| X'  # type: str
O = '| O'  # type: str

turn = int(input('X - 1 or O - 0 first? '))
if turn == 1:
    turn = X
else:
    turn = O

while t:
    check = ttm.make_turn(mas, a, b, turn)
    ttm.print_grid(mas)
    if check:
        t = False
    if turn == O:
        turn = X
    else:
        turn = O
