import random as rand

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

difficulty = ''
while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == 'easy':
    attempts = 10 
else:
    attempts = 5


trueNumber = rand.randint(1, 100)
guess = 0
while guess != trueNumber and attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == trueNumber:
        print("You got it right!")
    elif guess < trueNumber:
        print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("Too high.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

if guess == trueNumber:
    print("You win!")
else:
    print("You lose.")
