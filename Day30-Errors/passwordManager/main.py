import tkinter as tk
from json import JSONDecodeError
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.delete(0,tk.END)
    pass_entry.insert(tk.END, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# save data into data.txt
def save():
    web = web_entry.get()
    usr = name_entry.get()
    psw = pass_entry.get()
    new_data = {
        web: {
            'email': usr,
            'password': psw
        }
    }

    valid_fields = len(web) > 0 and len(usr) > 0 and len(psw) > 0
    if valid_fields:
        is_ok = True
    else:
        messagebox.showinfo(title='Oops',message='Please don\'t leave any fields empty!')
        is_ok = False

    if is_ok:
        data = {}
        try:
            with open(file='data.json',mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except (FileNotFoundError, JSONDecodeError):
            data = new_data
        finally:
            with open(file='data.json',mode='w') as file:
                json.dump(data, file, indent=4)
            #Clear website and psw contents
            web_entry.delete(0,tk.END)
            pass_entry.delete(0, tk.END)


# ---------------------------- LOOKUP INFO ------------------------------- #
def find_password():
    web = web_entry.get()
    header = ''
    text = ''
    try:
        with open(file='data.json',mode='r') as file:
            data = json.load(file)
        entry = data[web]
    except FileNotFoundError:
        header = 'Error'
        text = 'No Data File Found'
    except KeyError:
        header = 'Error'
        text = 'No details for the website exists'
    else:
        usr = entry['email']
        psw = entry['password']
        text = f'Email: {usr}\nPassword: {psw}'
        header = web
    finally:
        messagebox.showinfo(title=header, message=text)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
# window.minsize(240,240)
window.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=200,height=200)
img = tk.PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

# Website Label
web_label = tk.Label(text='Website', )
web_label.grid(column=0,row=1, sticky=tk.E)

# Website Entry
web_entry = tk.Entry(width=32)
web_entry.grid(column=1,row=1, columnspan=2, sticky=tk.W)
web_entry.focus()

# Email/Username label
name_label = tk.Label(text='Email/Username')
name_label.grid(column=0,row=2, sticky=tk.E)

# Email/Username Entry
name_entry = tk.Entry(width=36)
name_entry.grid(column=1,row=2, columnspan=2, sticky=tk.W)
name_entry.insert(tk.END, 'hello world')

# Password Label
pass_label = tk.Label(text='Password')
pass_label.grid(column=0,row=3, sticky=tk.E)

# Password Entry
pass_entry = tk.Entry(width=32)
pass_entry.grid(column=1,row=3, sticky=tk.W)

# Generate Pass Button
pass_button = tk.Button(text='Generate Password', command=generate_password)
pass_button.grid(column=2,row=3, sticky=tk.W)

# Add Button
add_button = tk.Button(text='Add', width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2, sticky=tk.W)

# Search Button
search_button = tk.Button(text='Search', command=find_password, width=14)
search_button.grid(column=2,row=1,sticky=tk.W)

window.mainloop()