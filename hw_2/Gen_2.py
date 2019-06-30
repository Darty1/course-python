def chain(*args):
    i = 0
    while i < len(args):  # а зачем while? можно ж было использовать for arg in args
        yield args[i]
        i += 1


# идея chain в том, чтобы сцепить несколько перечислений в одно
# нужно было так:
def chain2(*args):
    for arg in args:
        for item in arg:
            yield item


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x)


