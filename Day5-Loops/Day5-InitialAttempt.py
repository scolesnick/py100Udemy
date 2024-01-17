import random as r
import string as s

print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in your password?\n'))

symbols = int(input('How many symbols would you like?\n'))
numbers = int(input('How many numbers would you like?\n'))

total = letters + symbols + numbers
password = ''

for i in range(total+1):
    n = r.choice([1,2,3])
    if n == 1 and letters != 0:
        password += r.choice(s.ascii_letters)
        letters -= 1
    elif n == 2 and symbols != 0:
        password += r.choice(s.punctuation)
        symbols -= 1
    elif n == 3 and numbers != 0:
        password += r.choice(s.digits)
        numbers -= 1
    else:
        i += 1

print(f'Here is your password: {password}')