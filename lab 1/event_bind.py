from tkinter import *
from tkinter.ttk import *

def add_one():
    value.set(value.get() + 1)
    
def wow(event):
    label2.config(text="WWWWOOOOWWWW")
    
window = Tk()
value = IntVar(window, 0)

label = Label(window, textvariable=value) # uses the command option to identify a simple zero-parameter function
label.pack()
label2 = Label(window) # call to the function "wow" when the user completes the action specified in the event descriptor on the widget
label2.pack()

button = Button(window, text="Add one", command=add_one)
button.bind("<Shift-Double-Button-1>", wow)
button.pack()

window.mainloop()