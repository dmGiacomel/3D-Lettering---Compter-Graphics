from tkinter import *
from random import randint
from letter_representation import *
import numpy as np
import math

VRP_f = (0, 0, 20)
VRP_l = (20, 0, 0)
VRP_t = (0, 20, 0)
VRP_p = (10, 10, 10)
P_f = (0, 0, 5)
P_l = (5, 0, 0)
P_t = (0, 5, 0)
P_p = (0, 0, 0)
viewUp = (0, 1, 0)

def rgb(r, g, b):
    return ("#{:02x}{:02x}{:02x}".format(r, g, b))

def pipeline(VRP, P, u, v, x, y, dp, points, opc):
    VRP_N = np.array([-VRP[0], -VRP[1], -VRP[2]])

    vec_n = np.array([VRP[0] - P[0], VRP[1] - P[1], VRP[2] - P[2]])
    norm_n = np.linalg.norm(vec_n)
    vec_n = vec_n / norm_n

    viewUp_local = viewUp
    if(opc == 't'):
        viewUp_local = (0, 0, -1)
        

    YxN = np.dot(viewUp_local, vec_n)
    YxNxN = YxN * vec_n
    vec_v = viewUp_local - YxNxN
    # print(vec_v)
    norm_v = np.linalg.norm(vec_v)
    print(vec_v, norm_v)
    vec_v /= norm_v
    # print(vec_v)

    vec_u = np.cross(vec_v, vec_n)

    matrix_SRUSRC = np.array([[vec_u[0], vec_u[1], vec_u[2], np.dot(VRP_N, vec_u)],
                         [vec_v[0], vec_v[1], vec_v[2], np.dot(VRP_N, vec_v)],
                         [vec_n[0], vec_n[1], vec_n[2], np.dot(VRP_N, vec_n)],
                         [0, 0, 0, 1]])

    matrix_pers = np.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, -1/dp, 0]])

    if(opc != 'p'):
        matrix_pers = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 1]])


    matrix_jp = np.array([[(u[1] - u[0])/(x[1] - x[0]), 0, 0, (-x[0]) * ((u[1] - u[0])/(x[1] - x[0])) + u[0]],
                         [0, (v[0] - v[1])/(y[1] - y[0]), 0, y[0] * ((v[1] - v[0])/(y[1] - y[0])) + v[1]],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    
    matrix_SRUSRT = np.matmul(np.matmul(matrix_jp, matrix_pers), matrix_SRUSRC)
    np.set_printoptions(suppress=True)
    #print("Matriz sru srt = ", matrix_SRUSRT)

    new_points = np.matmul(matrix_SRUSRT, points)

    for i in range(0, 2):
         coluna_escolhida = new_points[:, i]
         valor_divisao = new_points[3, i]
         new_points[:, i] = np.round(coluna_escolhida / valor_divisao)

    return new_points


def converter_pontos(object_to_convert, width, widthm1, height, heightm1, u, v, opc):
    aux = 0
    VRP = VRP_f
    P = P_f
    if(opc == 'f'):
        VRP = VRP_f
        P = P_f
    elif(opc == 'l'):
        VRP = VRP_l
        P = P_l
    elif(opc == 't'):
        VRP = VRP_t
        P = P_t
    elif(opc == 'p'):
        VRP = VRP_p
        P = P_p
    dp = 3
    for i in object_to_convert.faces:
        for j in i.arestas:
            if(j.v1.convert == 0 and j.v2.convert == 0): # nenhum dos dois vertices foi convertido
                pontos_2_convert = np.array([[j.v1.x, j.v2.x],
                                            [j.v1.y, j.v2.y],
                                            [j.v1.z, j.v2.z],
                                            [1, 1]])
                pontos_2_convert = pipeline(VRP, P, (width, widthm1), (height, heightm1), u, v, dp, pontos_2_convert, opc)                
                j.v1.x, j.v1.y, j.v1.z = pontos_2_convert[0, 0], pontos_2_convert[1, 0], pontos_2_convert[2, 0]
                j.v2.x, j.v2.y, j.v2.z = pontos_2_convert[0, 1], pontos_2_convert[1, 1], pontos_2_convert[2, 1]
                j.v1.convert = 1
                j.v2.convert = 1
            elif(j.v1.convert == 1 and j.v2.convert == 0): # v2 ainda nao foi convertido
                pontos_2_convert = np.array([[1, j.v2.x],
                                            [1, j.v2.y],
                                            [1, j.v2.z],
                                            [1, 1]])
                pontos_2_convert = pipeline(VRP, P, (width, widthm1), (height, heightm1), u, v, dp, pontos_2_convert, opc)                
                #j.v1.x, j.v1.y, j.v1.z = pontos_2_convert[0, 0], pontos_2_convert[1, 0], pontos_2_convert[2, 0]
                j.v2.x, j.v2.y, j.v2.z = pontos_2_convert[0, 1], pontos_2_convert[1, 1], pontos_2_convert[2, 1]
                j.v2.convert = 1
            elif(j.v1.convert == 0 and j.v2.convert == 1): # v1 ainda nao foi convertido
                pontos_2_convert = np.array([[j.v1.x, 1],
                                            [j.v1.y, 1],
                                            [j.v1.z, 1],
                                            [1, 1]])
                pontos_2_convert = pipeline(VRP, P, (width, widthm1), (height, heightm1), u, v, dp, pontos_2_convert, opc)                
                j.v1.x, j.v1.y, j.v1.z = pontos_2_convert[0, 0], pontos_2_convert[1, 0], pontos_2_convert[2, 0]
                j.v1.convert = 1
                #j.v2.x, j.v2.y, j.v2.z = pontos_2_convert[0, 1], pontos_2_convert[1, 1], pontos_2_convert[2, 1]
        aux += 1

    return object_to_convert

def desenhar_objeto(canvas, objeto, cor):
    for i in objeto.faces:
            for j in i.arestas:
                canvas.create_line(j.v1.x, j.v1.y, j.v2.x, j.v2.y, fill=rgb(cor[0], cor[1], cor[2]), width=2)
                print(j.v1.x, j.v1.y, j.v2.x, j.v2.y)
    canvas.pack()

class Window:
    def __init__(self, Wnd):
        Wnd.resizable(width = False, height = False)
        Wnd.title("Tabajara Painter")
        self.canvas = Canvas(Wnd, width = 1820, height = 1000, bg = rgb(200, 200, 200), highlightthickness=1, highlightbackground="black")
        self.canvas.pack()

        letra = "./letras_numeros/0_norm.txt"

        object_front = Letra(letra)
        object_lateral = Letra(letra)
        object_top = Letra(letra)
        object_pers = Letra(letra)
        #print(object_to_write.faces[0].arestas[0].v1.x)

        widthm1 = self.canvas.winfo_reqwidth() - 400
        heightm1 = self.canvas.winfo_reqheight() - 400
        u = (-4, 4)
        v = (-2, 2)

        cor = (0, 0, 0)

        object_front = converter_pontos(object_front, 0, widthm1-200, 0, heightm1, u, v, 'f')
        desenhar_objeto(self.canvas, object_front, cor)

        object_lateral = converter_pontos(object_lateral, 800, widthm1 + 400, 0, heightm1, u, v, 'l')
        desenhar_objeto(self.canvas, object_lateral, cor)


        object_top = converter_pontos(object_top, 0, widthm1-200, 300, heightm1+300, u, v, 't')
        desenhar_objeto(self.canvas, object_top, cor)

        # u = (-0.5, 0.5)
        # v = (-0.5, 0.5)
        object_pers = converter_pontos(object_pers, 100, widthm1+500, 300, heightm1+300, u, v, 'p')
        desenhar_objeto(self.canvas, object_pers, cor)



mainWindow = Tk()
wind = Window(mainWindow)
# tupla_window = getWindowCoordinates(wind.canvas)
#tupla_viewport = getViewportCoordinates(wind.canvas, wind.Frm1)
# pontos = np.array([[30, 35],
#                    [2, 4],
#                    [25, 20],
#                    [1, 1]   
# ])
# matriz = pipeline((50, 15, 30), (20, 6, 15), (0, 320), (0, 240), (-8, 8), (-5, 5), 17, pontos)
# print(matriz)
mainWindow.mainloop()
