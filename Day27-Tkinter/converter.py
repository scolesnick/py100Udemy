import tkinter

window = tkinter.Tk()
window.title('Mile to KM Converter')
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)


miles = 0
km = 0
# Elements will be in a 3x3 grid

# Label for miles
label_mi = tkinter.Label(text='Miles')
label_mi.grid(column=2, row=0)

# Entry for miles
entry = tkinter.Entry(width=7)
# entry.insert(string='0')
entry.grid(column=1,row=0)

# Label for KM
label_km = tkinter.Label(text='Km')
label_km.grid(column=2, row=1)

# Label for Converted KM
label_c_km = tkinter.Label(text='0')
label_c_km.grid(column=1, row=1)


# Label for 'is equal to'
label = tkinter.Label(text='is equal to')
label.grid(column=0, row=1)


# Calculate button
def convert():
    val = float(entry.get())
    val*=1.609344
    label_c_km.config(text=str(val))

button = tkinter.Button(text='Calculate', command=convert)
button.grid(column=1,row=2)


window.mainloop()