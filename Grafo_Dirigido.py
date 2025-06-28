
class Grafo:
    def __init__(self, arquivo: str):
        self.vertices = []
        self.arestas = []
        self.rotulo_dict = dict()
        self.rotulo_to_index = dict()
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
    def rotuloToIndex(self, rotulo):
        return self.rotulo_to_index[rotulo]

    def vizinhos(self, v):
        return self.vizinhos_dict[v]

    def haAresta(self, u, v):
        # considerando que começa em 1 e nao 0
        if self.matrix[u - 1][v - 1] != float("inf"):
            return True
        return False

    def peso(self, u, v):
        return self.matrix[u - 1][v - 1]

    def ler(self, arquivo):
        # Formato esperado do arquivo:
        # *vertices n
        # 1 rotulo_1
        # 2 rotulo_2
        # ...
        # *arcs
        # a b peso
        # a c peso
        with open(arquivo, "r") as f:
            lines = f.readlines()

        # Lê o número de vértices
        if not lines or not lines[0].startswith("*vertices"):
            raise ValueError("Arquivo mal formatado: linha 0 deveria conter '*vertices n'")
        
        try:
            n_vertices = int(lines[0].split()[-1])
        except ValueError:
            raise ValueError("Número de vértices inválido")

        self.n_vertices = n_vertices
        self.vertices = []
        self.arestas = []
        self.rotulo_dict = {}
        self.vizinhos_dict = {}
        self.n_arestas = 0

        # Inicializa a matriz de adjacência com infinito
        self.matrix = [
            [float("inf") for _ in range(n_vertices)] for _ in range(n_vertices)
        ]

        # Lê os vértices (linhas de 1 até n_vertices)
        for i in range(1, n_vertices + 1):
            line = lines[i].strip()
            if not line:
                continue

            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue  # linha mal formatada

            try:
                numero = int(parts[0])
                rotulo = parts[1]
            except ValueError:
                continue

            self.vertices.append(numero)
            self.rotulo_dict[numero] = rotulo
            self.rotulo_to_index[rotulo] = numero
            self.vizinhos_dict[numero] = []

        # Lê as arestas (a partir da linha '*edges')
        # Procura a linha que começa com '*edges'
        inicio_arestas = -1
        for idx, line in enumerate(lines):
            if line.strip().lower() == "*arcs":
                inicio_arestas = idx + 1
                break

        if inicio_arestas == -1:
            raise ValueError("Arquivo não contém seção '*edges'")

        # Processa as arestas
        for i in range(inicio_arestas, len(lines)):
            line = lines[i].strip()
            if not line:
                continue

            tokens = line.split()
            if len(tokens) < 3:
                continue  # pula linhas incompletas

            try:
                a = int(tokens[0])
                b = int(tokens[1])
                peso = float(tokens[2])
            except ValueError:
                continue

            self.vizinhos_dict[a].append(b)
            #self.vizinhos_dict[b].append(a)

            self.arestas.append((a, b))
            self.matrix[a - 1][b - 1] = peso
            #self.matrix[b - 1][a - 1] = peso
            self.n_arestas += 1
