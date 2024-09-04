#create add() func to take an unlimited number of args
# use a loop to sum all of the args in the func
from numpy.ma.core import multiply


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,6))
print(add(5,5,5))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(n = 2, add = 3, multiply = 5)