from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

# Configuration
configuration = "dynamic"  # Change to "static" for static keyboard

# Record the start time
start = time.time()
# Number of times going through a block
n = 2
# Number of letters for each round
num_letters = 3
# This [] is created to store the letters selected for each round
block = []
# This [] is created to add the letters selected in total
num_blocks = []
letter_shown = {}
letters = list('abcdefghijklmnopqrstuvwxyz')

while len(block) != num_letters:
    # Randomly select the letter from list of letters, then pop it from oringal list and append it into new block
    letter_selected = letters[random.randrange(0, len(letters))]
    letters.pop(letters.index(letter_selected))
    block.append(letter_selected)

# Repeat the block n times and shuffle to create a list of num_blocks
while n > 0:
    random.shuffle(block)
    num_blocks += block
    n -= 1

# Initial letter to find
letter_found = num_blocks[0]

def letter_count(letter_found, letter_shown):
    # Count the number of times a letter is found
    if letter_found not in letter_shown:
        letter_shown[letter_found] = 1 # If the number is frist time to shown, mark it as 1
    else:
        letter_shown[letter_found] += 1 # Otherwise count += 1

def clickButton(character_clicked, letter_to_find):
    global configuration
    global start
    global letter_shown
    global num_blocks

    if character_clicked == letter_to_find:
        # Calculate the total time taken to the correct letter
        total_time = "{:.1f}".format((time.time() - start) * 1000)
        # Record the click count and time in the letter_shown dictionary
        letter_count(letter_to_find, letter_shown)
        # Write the data to the CSV file
        with open('experiment_{}_log.csv'.format(configuration), 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["Yann", configuration, letter_to_find, letter_shown[letter_to_find], total_time])
        num_blocks.pop(0)  # Remove the found letter from the list
        if not num_blocks:
            labeltext.set("Now, you finished all blocks.")
        else:
            letter_to_find = num_blocks[0]
            labeltext.set(letter_to_find)
            if configuration == "dynamic":
                # Update the keyboard layout if configuration is set as dynamic
                board = generate_keyboard()
                create_keyboard(board, frame, letter_to_find)
            start = time.time()

def create_keyboard(board, frame, letter_to_find):
    # Clear the existing buttons
    for widget in frame.winfo_children():
        widget.destroy()

    # Create the keyboard layout with buttons
    for i in range(len(board)):
        for j in range(len(board[i])):
            buttonframe = Frame(frame, height=64, width=64)
            buttonframe.grid(column=(2 * j) + i, row=i, columnspan=2)
            buttonframe.pack_propagate(0)
            button = Button(buttonframe, text=board[i][j], command=lambda x=board[i][j], y=letter_to_find: clickButton(x, y))
            button.pack(fill=BOTH, expand=1)

def generate_keyboard():
    # Generate a randomized keyboard layout
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_alphabet = list(alphabet)
    random.shuffle(list_alphabet)
    first_row = ''.join(list_alphabet[0:10])
    second_row = ''.join(list_alphabet[10:19])
    third_row = ''.join(list_alphabet[19:])
    board = [first_row, second_row, third_row]
    return board

# Open the CSV file for writing (include header)
with open('experiment_{}_log.csv'.format(configuration), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Name", "Configuration", "Letter Found", "Letter Shown Count", "Total Time (ms)"])

# Create the main GUI window
window = Tk()
frame = Frame(window, borderwidth=1, relief=RIDGE, height=32, width=32)
frame.pack(side=BOTTOM, padx=10, pady=10)

# Create a label to display the current letter to find
labeltext = StringVar()
label = Label(window, textvariable=labeltext)
labeltext.set(letter_found)
label.pack()

# Create the initial keyboard layout and populate it with buttons
board = generate_keyboard()
create_keyboard(board, frame, letter_found)

# Start the Tkinter main loop
window.mainloop()
