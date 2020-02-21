import sys
from _ctypes import ArgumentError


def flag(n):
    if n % 2 != 0:
        raise ArgumentError('The input N shall be an integer even number')
    st = '#' * (3 * n + 2) + '\n'
    for i in range(0, n // 2):
        st += '#' + 3 * n * ' ' + '#\n'
    k = n // 2 - 1
    s = 0
    for i in range(0, n):
        st += '#' + (n + k) * ' ' + '*' + s * 'o' + '*' + (n + k) * ' ' + '#\n'
        if k > 0 and i <= n // 2 - 1:
            k -= 1
            s += 2
        elif i > n // 2 - 1:
            k += 1
            s -= 2
    for i in range(0, n // 2):
        st += '#' + 3 * n * ' ' + '#\n'

    st += '#' * (3 * n + 2) + '\n'
    return st


N = int(sys.argv[1])
print(flag(N))
