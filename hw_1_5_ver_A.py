s = str(input('Input:  '))
l = int(len(s))
tokens = []
while True:
    for i in range(l):
        if s[i] not in {'+', '-', '*', '/'}:
            continue
        tokens += float(s[:i]), s[i]
        s = s[i+1:]
        break
    else:
        tokens += float(s),
        break
<<<<<<< HEAD
=======

>>>>>>> origin/master
i = 1
while i < len(tokens) - 1:
    token = tokens[i]
    if token == '*':
        tokens[i - 1] *= tokens[i + 1]
        del tokens[i:i+2]
    elif token == '/':
        tokens[i - 1] /= tokens[i+1]
        del tokens[i:i + 2]
    else:
        i += 1

i = 1
while i < len(tokens) - 1:
    token = tokens[i]
    if token == '+':
        token[i - 1] += tokens[i + 1]
        del tokens[i:i+2]
    elif token == '-':
        tokens[i - 1] -= tokens[i +1]
        del tokens[i:i + 2]
    else:
        i += 1

assert len(tokens) == 1
print(tokens[0])