import physics as phy
import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

class App(tk.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        master.config(bg=bg_c)
        self.create_widgets()
        master.update()
        self.create_Spring()
        print(self.middle_of_canvas())


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

        self.Canvas.bind( "<Button-1>", self.pressed)
        self.Canvas.bind( "<B1-Motion>", self.pressed)
        self.Canvas.bind( "<ButtonRelease-1>", self.released)

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
        fig_canvas = FigureCanvasTkAgg(fig,self.master)
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

    
    def create_Spring(self):
        p_middle = self.middle_of_canvas()
        length = 100
        p_rest = phy.vector2d(p_middle.x+int(length), (p_middle.y))
        v_spring = p_rest-p_middle
        self.Spring = phy.Spring(v_spring)
        self.Spring.draw(self.Canvas,p_middle, p_rest)
        print(self.Spring.F)
##### 

    def pressed(self,event):
        p_mouse = phy.vector2d(int(self.Canvas.canvasx(event.x)), -int(self.Canvas.canvasx(event.y)))
        p_middle = self.middle_of_canvas()
        v_spring = p_mouse - p_middle
        force = self.Spring.force(v_spring)
        self.Spring.draw(self.Canvas,p_middle,p_mouse)
        return force, p_mouse

    def released(self,event): 
        force, p_mouse = self.pressed(event)
        print(force)
        force.draw(self.Canvas, p_mouse)
#### Helpers #####

    def middle_of_canvas(self):
        screen_width = self.master.winfo_width()
        screen_height = self.master.winfo_height()   
        middle_x = int(screen_width * 0.5 * 0.5)
        middle_y = int(screen_height * 0.9 * 0.5)  
        return phy.vector2d(middle_x,-middle_y)

#### MAIN ####

root = tk.Tk()

bg_c = 'black'
fg_c = 'white'

window_width = 1000
window_height = 600
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
root.title('Feder Vektorfelder')
root.attributes('-topmost')
myapp = App(root)
myapp.mainloop()