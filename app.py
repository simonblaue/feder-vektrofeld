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

        self.Canvas.bind( "<Button-1>", self.B1_pressed)
        self.Canvas.bind( "<B1-Motion>", self.B1_moved)


        middle = self.middle_of_canvas()
        self.SpringID = self.Canvas.create_line(middle.x,middle.y, middle.x+50, middle.y+50)
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

##### 
    def B1_pressed(self,event):
        p_mouse = phy.vector2d(int(self.Canvas.canvasx(event.x)), int(self.Canvas.canvasx(event.y)))
        p_middle = self.middle_of_canvas()
        v_spring = p_mouse - p_middle
        if self.SpringID == None:
            self.SpringID = self.Canvas.create_line(p_middle.x,p_middle.y,p_mouse.x,p_mouse.y)
        else:
            self.Canvas.coords(self.SpringID,p_middle.x,p_middle.y,p_mouse.x,p_mouse.y)
        
    def B1_moved(self,event):
        p_mouse = phy.vector2d(int(self.Canvas.canvasx(event.x)), int(self.Canvas.canvasx(event.y)))
        p_middle = self.middle_of_canvas()
        self.Canvas.coords(self.SpringID,p_middle.x,p_middle.y,p_mouse.x,p_mouse.y)

#### Helpers #####

    def middle_of_canvas(self):
        screen_width = self.master.winfo_width()
        screen_height = self.master.winfo_height()   
        middle_x = int(screen_width * 0.5 * 0.5)
        middle_y = int(screen_height * 0.9 * 0.5)  
        return phy.vector2d(middle_x,middle_y)
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