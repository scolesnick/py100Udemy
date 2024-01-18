# Hangman game
#   The final script includes ASCII art
#   This script will just include blanks with a number of guesses

word = 'beekeeper'

word_list = list(word)
guessed = []
for c in word_list:
    guessed.append('_')

# game over when word is guessed or out of hangman chances - arms, legs, body, head
chances = 6
win = False

while chances > 0 and not win:
    for c in guessed:
        print(c + ' ', end='')

    print('')
    letter = input('Guess a letter.\n')

    if letter.lower() in word_list:
        print(f'{word_list.count(letter.lower())} case(s) of the letter are in the word')
        indicies = [i for i, x in enumerate(word_list) if x == letter]
        for i in indicies:
            guessed[i] = letter
    else:
        print(f'{letter.lower()} is not a letter')
        chances -= 1
        print(f'You have {chances} remaining.')
    print('')
    if '_' not in guessed:
        win = True
        
if win:
    print(word)
    print('You win.')
else:
    print('You lose. :(')