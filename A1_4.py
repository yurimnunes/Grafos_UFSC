from A1_1 import Grafo
import math
import sys

def dijkstra(g: Grafo, s: int):
    n = g.qtdVertices()
    distancias = [math.inf] * n
    predecessores = [None] * n
    visitados = [False] * n

    distancias[s] = 0

    for _ in range(n - 1):
        u = vertice_mais_proximo(distancias, visitados)
        if u == -1:
            break  # Todos os acessíveis já foram visitados
        visitados[u] = True

        for viz in g.vizinhos(u + 1):
            v = viz - 1
            if not visitados[v] and g.haAresta(u + 1, viz):
                peso = g.peso(u + 1, viz)
                nova_dist = distancias[u] + peso
                if nova_dist < distancias[v]:
                    distancias[v] = nova_dist
                    predecessores[v] = u

    exibir_caminhos(distancias, predecessores)
    return distancias, predecessores

def vertice_mais_proximo(distancias, visitados):
    minimo, indice = math.inf, -1
    for i, d in enumerate(distancias):
        if not visitados[i] and d < minimo:
            minimo, indice = d, i
    return indice

def exibir_caminhos(distancias, predecessores):
    for v, d in enumerate(distancias):
        if d == math.inf:
            print(f"{v + 1}: ; d= inf")
            continue

        caminho = []
        atual = v
        while atual is not None:
            caminho.append(atual + 1)
            atual = predecessores[atual]
        caminho.reverse()

        caminho_str = ",".join(map(str, caminho))
        print(f"{v + 1}: {caminho_str}; d= {int(d)}")

def main():
    if len(sys.argv) != 3:
        print("Uso A1_4 (Dijkstra): python3 A1_2.py <arquivo_de_entrada> <vértice_de_origem>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    try:
        s = int(sys.argv[2]) - 1
    except ValueError:
        sys.exit(1)

    try:
        g = Grafo(arquivo_entrada)

        if not (0 <= s < g.qtdVertices()):
            sys.exit(1)

        dijkstra(g, s)

    except FileNotFoundError:
        sys.exit(1)
    except ValueError as e:
        sys.exit(1)

if __name__ == '__main__':
    main()
