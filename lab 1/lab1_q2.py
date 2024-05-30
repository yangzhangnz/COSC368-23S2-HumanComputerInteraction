from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("tk")

# Create a Text widget with 34 characters wide and 12 characters high
text_widget = Text(window, width=34, height=12, wrap=NONE)
text_widget.grid(row=0, column=0)

# Insert some text into the Text widget
initial_text = "This is a 2D scrolling window and this sentence only is used for testing.\n" * 50
text_widget.insert('1.0', initial_text)

# Create horizontal scrollbar
horizontal_scrollbar = Scrollbar(window, orient=HORIZONTAL, command=text_widget.xview)
horizontal_scrollbar.grid(row=1, column=0, sticky='ew')

# Create vertical scrollbar
vertical_scrollbar = Scrollbar(window, orient=VERTICAL, command=text_widget.yview)
vertical_scrollbar.grid(row=0, column=1, sticky='ns')

# Configure the Text widget to use the scrollbars
text_widget.config(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)

# Make the horizontal scrollbar expand horizontally to fill the available space
window.grid_rowconfigure(0, weight=1)# Bind the horizontal scrollbar to the Text widget for left and right scrolling
window.grid_columnconfigure(0, weight=1)

window.mainloop()
