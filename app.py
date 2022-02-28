import physics as phy
import tkinter as tk

import numpy as np

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class App(tk.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        master.config(bg=bg_c)
        self.create_widgets()
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
        self.master.update()
         # prepare data
        screen_width = self.master.winfo_width()
        screen_height = self.master.winfo_height()
        canvas_w = int(screen_width * 0.5)
        canvas_h = int(screen_height * 0.9)
        x = np.linspace(-spring_length,int(canvas_w/2-1),500)
        y = np.linspace(-spring_length,int(canvas_h/2-1),500)
        x_2d, y_2d = np.meshgrid(x,y)
        spring_pot = 1/2 * spring_k * np.sqrt(x_2d**2+y_2d**2)
        print('Value of f', spring_pot,'\n')
       

        # create figure
        fig = Figure(figsize=(6,4), dpi=100)
        fig_canvas = FigureCanvasTkAgg(fig,self.master)
        axes = fig.add_subplot(111, projection='3d')

        # create the barchart
        axes.plot_surface(x_2d,y_2d,spring_pot, cmap=cm.jet)
        axes.set_title('Das Federpotenzial')
        axes.set_ylabel('y-Auslenkung')
        axes.set_xlabel('x-Auslenkung')
        axes.set_zlabel('Potenzial')


        fig_canvas.get_tk_widget().place(
            relx=1,
            rely=0.05,
            relheight=0.9,
            relwidth=0.5,
            anchor = 'ne'
        )

    
    def create_Spring(self):
        p_middle = self.middle_of_canvas()
        p_rest = phy.vector2d(p_middle.x+int(spring_length), (p_middle.y))
        v_spring = p_rest-p_middle
        self.Spring = phy.Spring(v_spring, spring_k)
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

# Spring Values
spring_k = 0.5
spring_length = 100

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