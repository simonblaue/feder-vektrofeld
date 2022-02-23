import tkinter as tk
from tkinter import ttk
from turtle import bgcolor

class App(tk.Frame):
    
    def __init__(self,master):
       super().__init__(master)


    def create_widgets(self):
        self.Canvas = ttk.Canvas(self, width=50, height=50,bg=background_color)
        self.plotFrame = ttk.Frame(self, bg=background_color)

    def place_widgets(self):
        self.Canvas.place()
        self.plotFrame.place()



background_color = 'white'
root = tk.Tk()
window_width = 500
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

myapp = App(root)
myapp.mainloop()