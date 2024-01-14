print('Welcome to Treasure Island. \nYour mission is to find the treasure')

action = ''
alive = True

action = input('You\'r at a cross road. Where do you want to go? Type "left" or "right"\n')

if action != 'left':
    alive = False
    print('Fall into a hole.\nGame Over.')
else:
    action = input('You come across a lake, "swim" across or "wait"?\n')
if action != 'wait' and alive:
    print('Attacked by trout.\nGame Over.')
    alive = False
elif alive:
    action = input('You come across a house with 3 doors. One "red", one "yellow" and one "blue". Which door do you choose?\n')
if alive:
    if action == 'red':
        print('Burned by fire.\nGame Over')
    elif action =='blue':
        print('Eaten by beasts.\nGame Over')
    elif action =='yellow':
        print('You Win!')
    else:
        print('Game Over.')