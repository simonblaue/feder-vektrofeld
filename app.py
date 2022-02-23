import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()


    def create_widgets(self):

        #Canvas for Spring
        self.Canvas = tk.Canvas(
            self.master,
            bg='white',
            borderwidth=3
        )
        self.Canvas.place(
            relx=0.5,
            rely=0.05,
            relheight=0.9,
            relwidth=0.5,  
            anchor='ne'
        )

        # Matplotlib figure

         # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create figure
        fig = Figure(figsize=(6,4), dpi=100)
        # create TkFigureCanvas object
        fig_canvas = FigureCanvasTkAgg(fig,self.master)
        # create Toolbar
        NavigationToolbar2Tk(fig_canvas, self).master
        # create axes
        axes = fig.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        fig_canvas.get_tk_widget().place(
            relx=1,
            rely=0.05,
            relheight=0.9,
            relwidth=0.5,
            anchor = 'ne'
        )





#### MAIN ####

root = tk.Tk()

bg_c = 'black'
fg_c = 'white'

window_width = 800
window_height = 400
spacing = 10

canvas_w = int(window_height/2)-spacing
canvas_h = int(window_height/2)-spacing

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.resizable(False, False)
root.attributes('-topmost')
myapp = App(root)
myapp.mainloop()