import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config (padx=20,pady=20) #add space around elements

# Label
my_label = tkinter.Label(text='I am a Label', font=('Arial',24,'bold'))
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50) # add space around this widget

#Button
def button_clicked():
    txt = entry.get()
    my_label.config(text=txt)
    # print('I got clicked')

button = tkinter.Button(text='Click Me', command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

# Input
entry = tkinter.Entry(width = 10)
# entry.pack()
entry.grid(column=3,row=3)

#new button
button2 = tkinter.Button(text='New Button')
button2.grid(column=2,row=0)

window.mainloop()