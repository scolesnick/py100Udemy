print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
n = int(input('How many people to split the bill? '))
tip = 0

while tip != 10 | tip != 12 | tip != 15:
    tip = int(input('What percentage would you like to give? 10, 12, or 15? '))

tip /= 100
total = bill + bill*tip
each = total/n

print('Each person should pay: $'+str(each))