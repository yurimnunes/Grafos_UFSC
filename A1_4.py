from A1_1 import Grafo
import sys


def bellman_ford(g, s):
    dist = []
    pred = []
    w = g.matrix

    for v in range(g.qtdVertices() + 1):
        dist.append(float("inf"))
        pred.append(None)
    dist[s] = 0

    i = 1
    while i < g.qtdVertices():
        for u, v in g.arestas:
            if dist[u] + w[u - 1][v - 1] < dist[v]:
                dist[v] = dist[u] + w[u - 1][v - 1]
                pred[v] = u
        i += 1

    for u, v in g.arestas:
        if dist[u] + w[u - 1][v - 1] < dist[v]:
            print("Tem ciclo negativo.")

    for v in g.vertices:
        pred_list = []
        if dist[v] != float("inf"):
            u = v
            while u is not None:
                pred_list.insert(0, u)
                u = pred[u]
        lista_str = ",".join(map(str, pred_list))
        print(f"{v}: {lista_str}; d= {dist[v]}")


def main():
    if len(sys.argv) != 3:
        print(
            "Uso A1_4 (BellMan-Ford): python3 A1_4.py <nome_arquivo> <vertice_inicial>"
        )
        sys.exit(1)

    grafo_nome = sys.argv[1]
    v = int(sys.argv[2])

    g = Grafo(grafo_nome)

    bellman_ford(g, v)


if __name__ == "__main__":
    main()
