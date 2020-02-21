import sys
from random import randint, randrange
import secrets
import hashlib
import hmac
s = sys.argv[1:]
k = 1
for i in s:
    print(k, ':', i)
    k += 1
print('0 : Exit')
c_choice = randrange(1, len(s))
m = s[c_choice]
keys = secrets.token_hex(16)
c_key = hmac.new(keys.encode(), m.encode(), hashlib.sha256).hexdigest()
print('HMAC: ', c_key)

u_choice = int(input('Your turn: '))
print('Secret key: ', keys)
print('Comp turn: ', c_choice)
nc_key = hmac.new(keys.encode(), m.encode(), hashlib.sha256).hexdigest()
if c_key == nc_key:
    print('OK')
else:
    print('Error')
    sys.exit()
if u_choice == 0:
    sys.exit()
if u_choice > c_choice and (u_choice - c_choice) > 2:
    print('you win')
elif u_choice > c_choice and (u_choice - c_choice) <= 2:
    print('you lose')
elif u_choice < c_choice and (c_choice - u_choice) <= 2:
    print('you win')
elif u_choice < c_choice and (c_choice - u_choice) > 2:
    print('you lose')
elif u_choice == c_choice:
    print('its draw')







