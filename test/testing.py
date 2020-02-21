import re

text = 'a aa aaa aaaa aaaaa'
largest = ''
i = 1

while 1:
    m = re.search("(" + ("\w" * i) + ").*\\1.*\\1", text)
    if not m:
        print(m)
        break
    print(m)
    largest = m.group(1)
    i += 1

print(largest)
