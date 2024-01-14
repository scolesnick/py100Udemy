print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
n = int(input('How many people to split the bill? '))
tip = 0

while tip != 10 and tip !=12 and tip != 15:
    tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

tip /= 100
total = bill + bill*tip
each = round(total/n,2)
# Lecture showed formatting like:
#   "{:.2f}.format(total/n)"

print(f'Each person should pay: ${each}')