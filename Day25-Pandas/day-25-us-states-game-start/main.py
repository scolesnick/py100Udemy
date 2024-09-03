import turtle
from turtle import Turtle
FONT = ("Courier", 10, "normal")
ALIGNMENT = 'center'

import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)



'''
State Name Guesser

Req.
1. Convert the guess to Title case
2. Check if the guess is among the 50 states
3. Write correct guesses onto the map
4. Use a loop to allow the user to keep guessing
5. Record the correct guesses in a list
6. Keep track of the score
'''

df = pandas.read_csv('50_states.csv')

tim = Turtle()
tim.hideturtle()
tim.penup()
game_is_on = True
correct_guesses = []
possible_answers = df.state.unique()

def draw_coor(val):
    sliced_df = df[df.state == val]
    x = sliced_df.x.to_list()[0]
    y = sliced_df.y.to_list()[0]
    coordinate = (x, y)
    tim.goto(coordinate)
    tim.write(arg=val, align=ALIGNMENT, font=FONT)



with open('correct_guesses.txt','r') as file:
    for line in file:
        ans = line.strip()
        if ans in possible_answers:
            correct_guesses.append(ans)
            draw_coor(ans)

while game_is_on:
    text = f'{len(correct_guesses)}/50 States Correct'
    answer_state = screen.textinput(title=text, prompt='What\'s another state\'s names?')
    # If no answer is given, assume game over
    if answer_state is None or answer_state == ' ' or answer_state == '':
        game_is_on = False
        break

    # Handle states with 2 words i.e. New Mexico
    words = answer_state.split(' ')
    guess = ''
    for w in words:
        guess += w[0].upper() + w[1:].lower() + ' '
    guess = guess.strip()
    check = guess in possible_answers

    if check:
        draw_coor(guess)
        correct_guesses.append(guess)

    # Check if game is over
    if len(correct_guesses) == 50:
        game_is_on = False

with open('correct_guesses.txt','w') as file:
    for g in correct_guesses:
        file.write(g+'\n')

screen.exitonclick()