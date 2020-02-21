import tictacmoduls as ttm
from random import *


a = random()
print(a)
fool = '|  '
a = 0
b = 0
p = ' '
t = True
check = True
X = '| X'  # type: str
O = '| O'  # type: str
mas = ['| 1', '| 2', '| 3', '| 4', X, '| 6', '| 7', '| 8', '| 9']
ttm.print_grid(mas)
turn = O
check = False
t = False
while not check:
    if t:
        check = ttm.comp_turn(mas)
        t = False
    else:
        check = ttm.make_turn(mas, O)
        t = True


