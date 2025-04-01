
class Grafo:
    def __init__(self, arquivo: str):
        self.vertices = []
        self.arestas = []
        self.rotulo_dict = dict()
        self.vizinhos_dict = dict()
        self.n_vertices = 0
        self.n_arestas = 0

        self.ler(arquivo)

    def qtdVertices(self):
        return self.n_vertices
    def qtdArestas(self):
        return self.n_arestas

    def grau(self, v):
        return len(self.vizinhos_dict[v])

    def rotulo(self, v):
        return self.rotulo_dict[v]

    def vizinhos(self, v):
        return self.vizinhos_dict[v]
    
    def haAresta(self, u, v):
        # considerando que começa em 1 e nao 0
        if self.matrix[u-1][v-1] != float('inf'):
            return True
        return False

    def peso(self, u, v):
        return self.matrix[u-1][v-1]

    def ler(self, arquivo):
        #*vertices n
        #1 rotulo_de_1
        #2 rotulo_de_2
        #*edges
        #a b valor_do_peso
        #a c valor_do_peso
        with open(arquivo, 'r') as f:
            lines = f.readlines()
            n_vertices = int(lines[0].split()[-1])
            # v = [1,2,3,4...]
            self.n_vertices = n_vertices

            # infinito se nao tem conexão
            self.matrix = [[ float('inf') for _ in range(n_vertices)] for _ in range(n_vertices)]
            # vertices
            print('Vertices')
            for i in range(1, n_vertices + 1):
                line = lines[i]
                for j in range(1, len(line)):
                    if line[j] == ' ': 
                        number = int(line[:j])
                        name = line[j+1:]
                        break
                print(line)
                self.vertices.append(number)
                # numero: rotulo
                self.rotulo_dict[number] = name

                # vizinhos # aproveitei o loob pra criacao
                self.vizinhos_dict[number] = []
            # edges
            print('Arestas')
            for i in range(n_vertices + 2, len(lines)):

                #####
                line = lines[i].split()
                print(line)
                a = int(line[0])
                b = int(line[1])
                peso = float(line[2])

                self.vizinhos_dict[a].append(b)
                self.vizinhos_dict[b].append(a)

                self.arestas.append((a, b))
                self.matrix[a-1][b-1] = peso
                # é não dirigido
                self.matrix[b-1][a-1] = peso
                self.n_arestas += 1
            


                
if __name__ == "__main__":
    g = Grafo("ContemCicloEuleriano2.net")
    print("##########################")
    print(" FUNÇÕES DE TESTE")
    print('quantidade de vertices:', g.qtdVertices())
    print('quantidade de arestas:', g.qtdArestas())
    print('grau do vertice 1:', g.grau(1))
    print('rotulo do vertice 1:', g.rotulo(1))
    print('vizinhos do vertice 1:', g.vizinhos(1))
    print('ha aresta 1 2:', g.haAresta(1, 2))
    print('peso da aresta 1 2:', g.peso(1, 2))
    print("Verificar matrix")
    # ta feio, só quis mostrar
    arr =  [i*1.0 for i in range(1,10)]
    for i in range(0,g.qtdVertices()+1):
        print(f'{i} ', end= " "*3) 
    else:
        print()
    i = 1
    for line in g.matrix:
        print(i, line)
        i += 1
                


