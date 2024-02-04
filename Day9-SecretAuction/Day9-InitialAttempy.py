import os

print('Welcome to the secret auction program.')

bidders = {}

others = 'yes'
while others.lower() == 'yes':
    name = input('What is your name?: ')
    bid = float(input('What is your bid?: $'))
    others = input('Are there any other bidders? Type \'yes\' or \'no\' \n')
    bidders[name] = bid
    os.system('cls')

highest = ''
highest_val = 0.0

# Print the winner (who had the highest bid)
for k,v in bidders.items():
    if v > highest_val:
        highest_val =v
        highest = k

print(f'The winner is {highest} with a bid of ${highest_val}.')