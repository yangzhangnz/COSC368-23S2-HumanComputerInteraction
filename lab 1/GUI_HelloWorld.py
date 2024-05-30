from tkinter import* # make everything available from Python packages tkinter and from ttk.
from tkinter.ttk import* # Ttk provides a set of 'themed' widgets that update the original tkinter widgets, allowing styles to be applied to widgets.

window = Tk() # The invocation to Tk() on line 3 creates a root window and initialises Tk's capabilities.
data = StringVar() # creates a StringVar, which is a special Tk class supporting mutable strings.
data.set("Data to display") # sets the value of the string.

label = Label(window, textvariable = data) # creates a Label widget that is a child of the root window. The label is instructed to display text in the variable data.
label.grid(row = 0, column = 0) # uses a grid for geometry management, which assigns the widget into the smallest space required to properly display the widget on the first (zeroth) row and column. 

entry = Entry(window, textvariable = data) # creates an Entry widget that can be used to enter text. The widget is instructed to display and control the content of the variable data.
entry.grid(row = 1, column = 0) # uses a grid for geometry management again, packing the widget into its parent (the window).

window.mainloop() # initiates the main loop, which is an infinite loop that continually awaits user input on the GUI and allows user events on widgets (such as typing in the Entry widget) to be processed.

clear = Button(window, text= "Clear", command = lambda: clear_data(data))
clear.grid(row = 2, column = 0)
quit = Button(window, text= "Quit", command = window.destroy)
quit.grid(row = 3, column = 0)

s = Style() # makes s refer to a Style object from ttk.
s.configure("TButton", font = "helvetica 24", foreground = "green") # configures the style object so that all 'Tbutton' objects (all ttk buttons) have a large helvetica font with a green foreground.