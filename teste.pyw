#_*_ coding: cp1252 _*_
from tkinter import *
from random import randint
from winged_edge import *

def rgb(r, g, b):
    return ("#{:02x}{:02x}{:02x}".format(r, g, b))

def paraCoordenadasDeTela(ponto, largura_maxima_menos_um, altura_maxima_menos_um, deslocamento = 0, escala = 1):
    ponto_tela_x = round((ponto[0] * largura_maxima_menos_um + deslocamento) * escala)
    ponto_tela_y = round((ponto[1] * altura_maxima_menos_um + deslocamento) * escala)
    ponto_tela = (ponto_tela_x, ponto_tela_y)
    return ponto_tela



class Window:
    def __init__(self, Wnd):
        Wnd.resizable(width = False, height = False)
        Wnd.title("Tabajara Painter")
        self.canvas = Canvas(Wnd, width = 300, height = 300, bg = rgb(200, 200, 200), cursor = "hand2", highlightthickness=1, highlightbackground="black")
        self.canvas.bind("<1>", self.draw)
        #self.canvas.bind("<1>", self.StartPol)
        #self.canvas.bind("<3>", self.EndPol)
        self.canvas.pack()
        self.Frm = Frame(Wnd)
        self.Frm.pack()

        self.textLbl = StringVar()
        self.textLbl.set("teste x e y")
        self.Lbl = Label(self.Frm, textvariable = self.textLbl, font = ("Verdana", "13", "bold"))
        self.Lbl.pack()


    def draw(self, event):
        x_ini = self.canvas.winfo_rootx()
        y_ini = self.canvas.winfo_rooty()
        widthm1, heightm1 = (self.canvas.winfo_width() - 1, self.canvas.winfo_height() - 1)

        a_winged_edge = WingedEdgeCaracter("a_norm.txt")

        arestas = []
        for i in a_winged_edge.arestas:
            #arestas.append((paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1), paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1)))
            arestas.append(paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1, 20, 0.4))
            arestas.append(paraCoordenadasDeTela((i.vertice_inicial.x, i.vertice_inicial.y), widthm1, heightm1, 20, 0.4))

        print(arestas)

        for i in range(0, len(arestas), 2): 
            self.canvas.create_line(arestas[i], arestas[i + 1], fill = rgb(255, 0, 0))



#---------------------------------------------------------------------------------------------------------------

mainWindow = Tk()
Window(mainWindow)
mainWindow.mainloop()
