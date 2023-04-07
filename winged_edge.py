class Vertice:

    def __init__(self, x=None, y=None, z=None, aresta_incidente=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if aresta_incidente is not None:
            self.aresta_incidente = aresta_incidente

class Face:

    def __init__ (self, aresta_de_fronteira):
        self.aresta_de_fronteira = aresta_de_fronteira 

    def __init__ (self):
        pass

class Aresta:

    def __init__ (self, vertice_inicial = None, vertice_final = None, face_esquerda=None, face_direita=None, vertice_face_esquerda_prev=None, vertice_face_esquerda_next=None, vertice_face_direta_prev=None, vertice_face_direta_next=None):
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.face_esquerda = face_esquerda
        self.face_direita = face_direita
        self.vertice_face_esquerda_prev = vertice_face_esquerda_prev
        self.vertice_face_esquerda_next = vertice_face_esquerda_next
        self.vertice_face_direta_next = vertice_face_direta_next
        self.vertice_face_direta_prev = vertice_face_direta_prev


class WingedEdgeCaracter:

    def __init__ (self, nome_arquivo):
        self.vertices = []
        self.arestas = []
        self.faces = []

        arquivo = open(nome_arquivo, "r")
        linhas = arquivo.readlines()
        arquivo.close()
        self.valores = [valor for i in linhas for valor in i.split()]
        self.valores = [s.strip() for s in self.valores]
        self.valores = [float(s) for s in self.valores]

        #extracao das coordenadas dos vertices do arquivo de entrada
        for i in range(1, int(self.valores[0] * 4), 4):
            self.vertices.append(Vertice((self.valores[i + 1] + 1)/2, (-self.valores[i + 2] + 1)/2, (self.valores[i + 3] + 1)/2, None))

        #print([vertice.x for vertice in self.vertices], [vertice.y for vertice in self.vertices],[vertice.z for vertice in self.vertices])

        #formacao das arestas
        for i in range(int(self.valores[0] * 4 + 1), len(self.valores), 2):
            ar = Aresta(self.vertices[int(self.valores[i])], self.vertices[int(self.valores[i + 1])], Face(), Face(), Vertice(), Vertice(), Vertice(), Vertice())
            self.arestas.append(ar)
        





'''
valor = range(10)
print([i if i == 2 else 0 for i in valor])
print([i for i in valor if i == 2])
'''
'''
teste = WingedEdgeCaracter("a_norm.txt")
#print(teste.valores)
'''