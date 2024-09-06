from tkinter import END, Tk, Label, Button, PhotoImage, Canvas
from unittest.mock import right

BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ('Ariel', 28, 'italic')
WORD_FONT = ('Ariel', 48, 'bold')


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
canvas.create_image(410, 263, image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

# Text on Card
lang_text = canvas.create_text(400,150,text='Language', fill='black', font=LANGUAGE_FONT)
word_text = canvas.create_text(400,260,text='Word', fill='black', font=WORD_FONT)


# Buttons
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, activebackground=BACKGROUND_COLOR)
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, activebackground=BACKGROUND_COLOR)
right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)







window.mainloop()