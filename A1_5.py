import sys
from A1_1 import Grafo

def floyd_warshall(grafo):
    n = grafo.qtdVertices()
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Inicializa a matriz de distâncias
    for i in range(n):
        for j in range(n):
            dist[i][j] = grafo.peso(i + 1, j + 1)  # Vértices são 1-based
        dist[i][i] = 0  # Distância para si mesmo é 0
    
    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def formatar_saida(matriz_dist):
    for i in range(len(matriz_dist)):
        linha = f"{i + 1}:"  # Vértice de origem (1-based)
        distancias = [str(int(matriz_dist[i][j])) if matriz_dist[i][j] != float('inf') else "∞" 
                      for j in range(len(matriz_dist[i]))]
        linha += ",".join(distancias)
        print(linha)

def main():
    if len(sys.argv) != 2:
        print("Uso: python A1_5.py <arquivo_grafo>")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    grafo = Grafo(arquivo)
    distancias = floyd_warshall(grafo)
    formatar_saida(distancias)

if __name__ == "__main__":
    main()