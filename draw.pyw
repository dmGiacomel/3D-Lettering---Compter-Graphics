from tkinter import *
from random import randint
from letter_representation import *

VRP_f = (0, 0, 20)
VRP_l = [20, 0, 0]
VRP_t = [0, 20, 0]
P_o = [0, 0, 1]
P_p = []

def rgb(r, g, b):
    return ("#{:02x}{:02x}{:02x}".format(r, g, b))

def getWindowCoordinates(Window):
    x_max = int(Window.winfo_reqwidth() / 2)
    y_max = int(Window.winfo_reqheight() / 2)
    print("x max = ", x_max)
    print("y max = ", y_max)

    x_min = - int(Window.winfo_reqwidth() / 2)
    y_min = - int(Window.winfo_reqheight() / 2)

    x = (x_min, x_max)
    print("x min = ", x_min)
    y = (y_min, y_max)
    print("y_min = ", y_min)

    return (x, y)

def getViewportCoordinates(canvas, frame):
    x, y = canvas.canvasx(frame.winfo_rootx()), canvas.canvasy(frame.winfo_rooty())
    x_max = x + frame.winfo_width()
    y_max = y + frame.winfo_height()
    
    print("x min = ", x, "x_max = ", x_max)
    print("y_min = ", y, " y _max = ", y_max)
    return (x, y, x_max, y_max)

def SRUtoSRC(VRP, P):
    pass

def SRCtoSRT(matrix, umin, umax, vmin, vmax, xmin, xmax, ymin, ymax):
    pass


class Window:
    def __init__(self, Wnd):
        Wnd.resizable(width = False, height = False)
        Wnd.title("Tabajara Painter")
        self.canvas = Canvas(Wnd, width = 700, height = 500, bg = rgb(200, 200, 200), cursor = "hand2", highlightthickness=1, highlightbackground="black")
        self.canvas.pack()
        self.Frm = Frame(Wnd, width=200, height=200, bg="blue")
        self.canvas.create_window(100, 100, window=self.Frm)
        self.Frm.pack()
        tupla_window = getWindowCoordinates(self.canvas)
        tupla_viewport = getViewportCoordinates(self.canvas, self.Frm)


mainWindow = Tk()
Window(mainWindow)
mainWindow.mainloop()