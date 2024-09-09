from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        # Window init
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # params
        check_img = PhotoImage(file='images/true.png')
        x_img = PhotoImage(file='images/false.png')
        self.score = 0
        self.question = 'tbd'

        # Create Buttons
        self.check_button = Button(image=check_img, highlightthickness=0,
                            bg=THEME_COLOR, borderwidth=0,
                            activebackground=THEME_COLOR)
        self.x_button = Button(image=x_img, highlightthickness=0,
                            bg=THEME_COLOR, borderwidth=0,
                            activebackground=THEME_COLOR)
        self.check_button.grid(column=0, row=2)
        self.x_button.grid(column=1, row=2)

        # Create Score Label
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', font=('Arial',12))
        self.score_label.grid(column=1,row=0)

        # Create Canvas for questions
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text=self.question, fill=THEME_COLOR, font=('Arial',20,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        self.window.mainloop()