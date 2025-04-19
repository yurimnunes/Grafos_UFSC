from A1_1 import Grafo
import sys


def encontra_ciclo_euleriano(g):
    stack = []
    ciclo = []
    arestas = set(g.arestas)
    vizinhos = {v: list(g.vizinhos(v)) for v in g.vertices}
    v = 1

    while len(stack) > 0 or len(vizinhos[v]) > 0:
        if len(vizinhos[v]) == 0:
            ciclo.append(v)
            v = stack.pop()
        else:
            stack.append(v)
            for u in vizinhos[v]:
                if (v, u) in arestas or (u, v) in arestas:
                    break
            if (v, u) in arestas:
                arestas.remove((v, u))
            if (u, v) in arestas:
                arestas.remove((u, v))
            vizinhos[v].remove(u)
            vizinhos[u].remove(v)
            v = u

    ciclo.append(v)

    if len(ciclo) <= 1 or ciclo[0] != ciclo[-1]:
        print(0)
    else:
        print(1)
        ciclo_str = ",".join(map(str, ciclo))
        print(ciclo_str)


def main():
    if len(sys.argv) != 2:
        print("Uso A1_3 (Encontrar Ciclo Euleriano): python3 A1_4.py <nome_arquivo>")
        sys.exit(1)

    grafo_nome = sys.argv[1]
    g = Grafo(grafo_nome)
    encontra_ciclo_euleriano(g)


if __name__ == "__main__":
    main()
