


ops = ['+','-','*','/']
def cal(n1,n2,o):
    """ Performs Calculation n1 o n2, where o expects an operator as a string +/-/*/\ """
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1*n2
    elif o == '/':
        return n1/n2
    else:
        return 'invalid operator'

again = ''
val = 0.0
while True: 
    if again == 'y':
        n1 = val
    else:
        n1 = float(input('What\'s the first number?: '))
    for o in ops:
        print(o)
    op = input('Pick an operation: ')
    n2 = float(input('What\'s the second number?: '))
    val = cal(n1,n2,op)
    print(f'{n1} {op} {n2} = {val}')
    again = input(f'Type \'y\' to continue calculating with {val}, or type \'n\' to start a new calculation: ')
