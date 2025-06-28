from Grafo_Dirigido import Grafo

def bfs(grafo, origem, destino, residual):
    marked = [False] * (grafo.qtdVertices() + 1)  
    queue = [origem]

    predecessor = dict()
    for v in grafo.vertices:
        predecessor[v] = None

    distancia = dict()
    for v in grafo.vertices:
        distancia[v] = float("inf")
    distancia[origem] = 0
    while queue:
        u = queue.pop(0)
        if not marked[u]:
            marked[u] = True
            for v in grafo.vizinhos(u):
                if grafo.peso(u, v) - residual[(u, v)] == 0: #ignoramos arestas saturadas
                    continue
                else:
                    if not marked[v]:
                        queue.append(v)
                    if distancia[v] > distancia[u]:
                        distancia[v] = distancia[u] + 1
                        predecessor[v] = u
    if not marked[destino]: #nao foi possivel acessar o destino agora
        return False
    else:
        caminho = [destino]
        u = destino
        while u is not origem:
            u = predecessor[u]
            caminho = [u] + caminho
        return caminho

def edmonds_karp(grafo, s, t):
    n = grafo.qtdVertices()
    fluxo_maximo = 0
    residual = dict()
    for u in grafo.arestas:
        residual[u] = 0

    #caminhpos_encontrasdos = []
    #fluxos_encontrados = []
    while True:
        caminho = bfs(grafo, s, t, residual)
        if not caminho: # if caminho is False
            break
        pesos = []
        for i in range(len(caminho) - 1):
            u = caminho[i]
            v = caminho[i + 1]
            pesos.append(grafo.peso(u, v) - residual[(u, v)])
        fluxo = min(pesos)
        fluxo_maximo += fluxo
        # Atualiza o grafo residual
        for i in range(len(caminho) - 1):
            u = caminho[i]
            v = caminho[i + 1]
            residual[(u, v)] += fluxo
    return fluxo_maximo
    
        


#grafo = Grafo("fluxo_prova_2025_1.net")

#s = grafo.rotulo_to_index["s"]
#t = grafo.rotulo_to_index["t"]
#residual = dict()
#for u in grafo.arestas:
#    residual[u] = 0
#res = bfs(grafo, s, t, residual)
#print(res)

#res = edmonds_karp(grafo, s, t)
#print("Fluxo máximo:", res)

def main():
    import sys
    if len(sys.argv) < 4:
        print("Uso: python3 A3_1.py <arquivo_grafo> <origem> <destino>")
        print("Exemplo: python3 A3_1.py fluxo.net s t")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    origem_str = sys.argv[2]
    destino_str = sys.argv[3]
    grafo = Grafo(arquivo)
    if origem_str.isdigit():
        s = int(origem_str)
    else:
        s = grafo.rotulo_to_index[origem_str]
        
    if destino_str.isdigit():
        t = int(destino_str)
    else:
        t = grafo.rotulo_to_index[destino_str]
    #s = grafo.rotulo_to_index[origem_str]
    #t = grafo.rotulo_to_index[destino_str]
    res = edmonds_karp(grafo, s, t)
    print(int(res))
if __name__ == "__main__":
    main()
    