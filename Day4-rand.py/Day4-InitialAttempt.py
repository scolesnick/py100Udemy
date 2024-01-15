# rock paper scissors
import random as rand

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
choices = {0:'Rock', 1:'Paper', 2:'Scissors'}
pc_choice = rand.randint(0,2)

print(f'You chose: {choices[choice]}')
print(f'Computer chose: {choices[pc_choice]}')

if (choice == pc_choice):
    print('It\'s a draw')
elif (choice == 0 and pc_choice == 1):
    print('You lose')
elif (choice == 0 and pc_choice == 2):
    print('You win')
elif (choice == 1 and pc_choice == 2):
    print('You lose')
elif (choice == 1 and pc_choice == 0):
    print('You win')
elif (choice == 2 and pc_choice == 0):
    print('You lose')
elif (choice == 2 and pc_choice == 1):
    print('You win')