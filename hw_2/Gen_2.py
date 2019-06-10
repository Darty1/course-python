def chain(*args):
    i = 0
    while i < len(args):
        yield args[i]
        i += 1


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x)


