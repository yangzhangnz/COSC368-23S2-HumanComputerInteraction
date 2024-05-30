from tkinter import *
from tkinter.ttk import *
import time
import random
import csv

class FittsExperiment:
    
    def __init__(self, master):
        self.master = master
        self.start_time = time.time()
        self.target_distances = [64, 128, 256, 512]
        self.canvas_width = 650
        self.canvas_height = 550
        self.output_file = open('fitts_experiment_results.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.output_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        self.target_widths = [8, 16, 32]
        self.all_combinations = self.generate_all_combinations()
        self.margin, self.corner1, self.target_distance, self.target_width = self.initial_setup()
        self.canvas, self.rect1, self.rect2 = self.setup_canvas(self.margin, self.corner1, self.target_distance)
        self.canvas.tag_bind(self.rect1, "<ButtonPress-1>", lambda event: self.click_rectangle(event, self.rect1))
        self.canvas.tag_bind(self.rect2, "<ButtonPress-1>", lambda event: self.click_rectangle(event, self.rect2))
        
        self.num_rounds = 4
        self.remaining_rounds = self.num_rounds
        self.one_counter = 1
        
        
    def initial_setup(self):
        # Calculate the initial positions and dimensions of rectangles
        target_distance, target_width = self.get_target_distance_and_width()
        total_span = target_distance + target_width
        margin = (self.canvas_width - total_span) / 2
        corner1 = margin + target_width
        return margin, corner1, target_distance, target_width

    def get_rect_colors(self, left_rect_color, right_rect_color):
        # Determine the color to be used for rectangles based on the current colors
        if left_rect_color == 'blue' and right_rect_color == 'green':
            right_color = 'blue'
            left_color = 'green'
        else:
            right_color = 'green'
            left_color = 'blue'
        return left_color, right_color

    def click_rectangle(self, event, rect):
        # Handle a click event on a rectangle
        total_time = "{:.1f}".format((time.time() - self.start_time) * 1000)
        self.log_time(total_time)
        self.one_counter += 1
        left_rect_color = self.canvas.itemcget(self.rect1, "fill")
        right_rect_color = self.canvas.itemcget(self.rect2, "fill")
        left_color, right_color = self.get_rect_colors(left_rect_color, right_rect_color)
        
        if self.remaining_rounds != 1:
            # Continue with the current target distance and width settings
            self.canvas.itemconfig(self.rect1, fill=left_color)
            self.canvas.itemconfig(self.rect2, fill=right_color)
            self.remaining_rounds -= 1
        else:
            # Switch to the next target distance and width settings
            if self.all_combinations:
                self.remaining_rounds = self.num_rounds
                margin, corner1, self.target_distance, self.target_width = self.initial_setup()
                self.canvas.coords(self.rect1, margin, 0, corner1, self.canvas_height)
                self.canvas.coords(self.rect2, margin + self.target_distance, 0, corner1 +self.target_distance, self.canvas_height)
                self.canvas.itemconfig(self.rect1, fill=left_color)
                self.canvas.itemconfig(self.rect2, fill=right_color)
                self.start_time = time.time()
            else:
                self.output_file.close()
                self.master.destroy()
        
    def setup_canvas(self, margin, corner1, target_distance):
        # Create the canvas and rectangles for the experiment
        canvas = Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        canvas.pack()
        rect1 = canvas.create_rectangle(margin, 0, corner1, self.canvas_height, fill="blue")
        rect2 = canvas.create_rectangle(margin + target_distance, 0, corner1 + target_distance, self.canvas_height, fill="green")
        return canvas, rect1, rect2
                    
    def log_time(self, total_time):
        # Log the time taken for each click to the CSV file
        if self.num_rounds == 1:
            self.csv_writer.writerow(["Participant", self.target_distance, self.target_width, self.one_counter, total_time])
        else:
            self.csv_writer.writerow(["Participant", self.target_distance, self.target_width, (self.num_rounds - self.remaining_rounds) + 1, total_time])            
        
    def generate_all_combinations(self):
        # Generate all combinations of target distances and widths for the experiment
        all_combinations = []  
        for distance in self.target_distances:
            for width in self.target_widths:
                all_combinations.append((distance, width))
        return all_combinations
    
    def get_target_distance_and_width(self):
        # Get a random combination of target distance and width
        random.shuffle(self.all_combinations)
        target_distance, target_width = self.all_combinations.pop(0)
        return target_distance, target_width
    
    
master = Tk()
fitts_experiment = FittsExperiment(master)
master.mainloop()
