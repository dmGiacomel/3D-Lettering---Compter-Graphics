class Vertice: 
    def __init__(self, x , y, z):
        self.x = x
        self.y = y
        self.z = z
        

class Aresta: 
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Face: 
    def __init__(self):
        pass

class Letra:
    def __init__(self, nome_arquivo):
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
            self.vertices.append(Vertice((self.valores[i + 1] + 1)/2, (-self.valores[i + 2] + 1)/2, (self.valores[i + 3] + 1)/2))
        
        #formacao das arestas
        print(int(self.valores[0] * 4 + 2))
        aux = 0
        for i in range(int(self.valores[0] * 4 + 2), int(self.valores[0] * 4 + 1) + int(self.valores[int(self.valores[0] * 4 + 1)] * 3), 3):
            self.arestas.append(Aresta(self.vertices[int(self.valores[i + 1])], self.vertices[int(self.valores[i + 2])]))

        # for i in self.arestas:
        #     print("aresta ", aux)
        #     aux = aux + 1
        #     print("vertice 1 = ", i.v1.x, i.v1.y, i.v1.z)
        #     print("vertice 2 = ", i.v2.x, i.v2.y, i.v2.z)

        # formacao das faces --> fazer depois!!
        #for i in range()

l = Letra("letras_numeros/0_norm.txt")
