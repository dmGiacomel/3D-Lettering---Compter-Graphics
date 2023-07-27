#_*_ coding: cp1252 _*_
from tkinter import *
from random import randint
from winged_edge import *

def rgb(r, g, b):
    return ("#{:02x}{:02x}{:02x}".format(r, g, b))

def paraCoordenadasDeTela(ponto, largura_maxima_menos_um, altura_maxima_menos_um, deslocamento_x = 0, deslocamento_y = 0, escala = 1):
    ponto_tela_x = round((ponto[0] * largura_maxima_menos_um + (deslocamento_x * largura_maxima_menos_um)) * escala)
    ponto_tela_y = round((ponto[1] * altura_maxima_menos_um + (deslocamento_y * altura_maxima_menos_um)) * escala)
    ponto_tela = (ponto_tela_x, ponto_tela_y)
    return ponto_tela



class Window:
    def __init__(self, Wnd):
        Wnd.resizable(width = False, height = False)
        Wnd.title("Tabajara Painter")
        self.canvas = Canvas(Wnd, width = 700, height = 500, bg = rgb(200, 200, 200), cursor = "hand2", highlightthickness=1, highlightbackground="black")
        self.canvas.pack()
        self.Frm = Frame(Wnd)
        self.Frm.pack()

        self.porcentagem = Entry(self.Frm, fg = "red", width = 5)
        self.porcentagem.pack(side = LEFT)

        self.Btn = Button(self.Frm, text = "escrever", command= lambda: self.draw(self), fg = "black", bg = "pink")
        self.Btn.pack(side = LEFT)


    def draw(self, event):
        self.canvas.delete("all")
        texto_entrada = self.porcentagem.get()
        letras = []
        for letra in texto_entrada:
             letras.append(letra)
        print(letras)
        # x_ini = self.canvas.winfo_rootx()
        # y_ini = self.canvas.winfo_rooty()
        widthm1, heightm1 = (self.canvas.winfo_width() - 1, self.canvas.winfo_height() - 1)
        deslocamentopx = 0.1

        for l in letras:
            if l == " ":
                deslocamentopx = deslocamentopx + 0.5
                continue

            arquivo = "letras_numeros/" + l + "_norm.txt"
            winged_edge = WingedEdgeCaracter(arquivo)
            arestas = []
            for i in winged_edge.arestas:
                #arestas.append((paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1), paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1)))
                arestas.append(paraCoordenadasDeTela((i.vertice_final.x, i.vertice_final.y), widthm1, heightm1, deslocamentopx, 0.1, 0.2))
                arestas.append(paraCoordenadasDeTela((i.vertice_inicial.x, i.vertice_inicial.y), widthm1, heightm1, deslocamentopx, 0.1, 0.2))
            for i in range(0, len(arestas), 2): 
                self.canvas.create_line(arestas[i], arestas[i + 1], fill = rgb(255, 0, 0))

            deslocamentopx = deslocamentopx + 1
            arestas.clear()

#---------------------------------------------------------------------------------------------------------------

mainWindow = Tk()
Window(mainWindow)
mainWindow.mainloop()
