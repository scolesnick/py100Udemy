from fileinput import filename
from tkinter import END, Tk, Label, Button, PhotoImage, Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ('Ariel', 28, 'italic')
WORD_FONT = ('Ariel', 48, 'bold')

start_lang = 'Click Button'
start_word = 'To Start'
timer = 0
current_card = {}
word_list = {}
df = None

# ---------------------------- Get Words ------------------------------- #
try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')
    df.to_csv('data/words_to_learn.csv', index=False)
finally:
    word_list = df.to_dict(orient='records')

# ---------------------------- Populate Words ------------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(lang_text, text='French',fill='black')
    canvas.itemconfig(word_text, text=current_card['French'],fill='black')
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(lang_text, text='English',fill='white')
    canvas.itemconfig(word_text, text=current_card['English'],fill='white')
    canvas.itemconfig(card_img, image=back_img)

# ---------------------------- Update Words ------------------------------- #
def check_press():
    # Check for start card
    if current_card == {}:
        next_card()
    else:
        word_list.remove(current_card)
        df2 = pandas.DataFrame(word_list)
        df2.to_csv('data/words_to_learn.csv', index=False, mode='w')
        next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)



# Set up images used
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')


# Card
canvas = Canvas(width=810, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(410, 263, image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

# Text on Card
lang_text = canvas.create_text(400, 150, text=start_lang, fill='black', font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 260, text=start_word, fill='black', font=WORD_FONT)


# Buttons
right_button = Button(image=right_img, highlightthickness=0,
                      bg=BACKGROUND_COLOR, borderwidth=0,
                      activebackground=BACKGROUND_COLOR, command=check_press)
wrong_button = Button(image=wrong_img, highlightthickness=0,
                      bg=BACKGROUND_COLOR, borderwidth=0,
                      activebackground=BACKGROUND_COLOR, command=next_card)
right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)

def dummy():
    pass
flip_timer = window.after(3000, func=dummy)

window.mainloop()