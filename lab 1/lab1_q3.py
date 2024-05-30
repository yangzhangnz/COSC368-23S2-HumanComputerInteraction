from tkinter import *

# Define the layout of the virtual keyboard
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

def append(char):
    """Insert the selected character into the entry box."""
    entry_box.insert(END, char)
    
def clear():
    """Clear the characters from the entry box."""
    entry_box.delete(0, END)

# Create the main window
window = Tk()
window.title("tk")

# Create a frame to hold the virtual keyboard
frame = Frame(window, borderwidth = 3, relief = RIDGE)
frame.pack(side = BOTTOM, padx = 10, pady = 10)

# Create a label to display the text entered in the entry box
label_text = StringVar()
label = Label(window, textvariable = label_text)
label.pack(side = LEFT, padx = 4)

# Create the entry box
entry_box = Entry(window, bd = 3, width = 28, font = 30)
entry_box.pack(side = LEFT)

# Create the clear button
clear_button = Button(window, text = 'Clear', command = clear)
clear_button.pack(side = RIGHT, padx = 10)

# Create the virtual keyboard buttons
for i in range(len(board)):
    for j in range(len(board[i])):
        button = Button(frame, text = board[i][j], command = lambda x = board[i][j]: append(x))
        button.grid(column = (2 * j) + i, row = i, columnspan = 2)

window.mainloop()
