import time
import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    top_label.config(text='Timer', fg=GREEN)
    canvas.itemconfigure(c_text, text='00:00')
    check_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = 60*WORK_MIN
    short_break_sec = 60*SHORT_BREAK_MIN
    long_break_sec = 60*LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text='Short Break', fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'

    canvas.itemconfigure(c_text, text=f'{min}:{sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checks = ''
        for _ in range(math.ceil(reps/2)):
            checks += '✔'
        check_label.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)

top_label = tk.Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36), highlightthickness=0)
top_label.grid(column=1,row=0)

canvas = tk.Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
c_text = canvas.create_text(100,130,text="00:00", fill='white',font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1,row=1)

start_button = tk.Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

check_label = tk.Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20, 'bold'), highlightthickness=0)
check_label.grid(column=1,row=3)


# update_clock(5)
# window.after(1000,update_clock)

window.mainloop()