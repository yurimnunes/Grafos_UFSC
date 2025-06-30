import sys
from A1_1 import Grafo


def hopcroft_karp(grafo):
    U = grafo.vertices[: grafo.qtdVertices() // 2]
    V = grafo.vertices[grafo.qtdVertices() // 2 :]
    M, dist = {}, {}

    def bfs():
        queue = []
        for u in U:
            if u not in M:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float("inf")
        dist[None] = float("inf")

        for u in queue:
            if dist[u] < dist[None]:
                for v in grafo.vizinhos(u):
                    m = M.get(v)
                    if dist.get(m, float("inf")) == float("inf"):
                        dist[m] = dist[u] + 1
                        queue.append(m)
        return dist[None] != float("inf")

    def dfs(u):
        if u is not None:
            for v in grafo.vizinhos(u):
                m = M.get(v)
                if dist.get(m, float("inf")) == dist[u] + 1 and dfs(m):
                    M[v] = u
                    M[u] = v
                    return True
            dist[u] = float("inf")
            return False
        return True

    while bfs():
        for u in U:
            if u not in M:
                dfs(u)

    return [(u, M[u]) for u in U if u in M and M[u] in V]


def main():
    if len(sys.argv) != 2:
        print("Uso A3_2 (Hopcroft Karp): python3 A3_2.py <nome_arquivo>")
        sys.exit(1)

    try:
        grafo = Grafo(sys.argv[1])
        emp = hopcroft_karp(grafo)
        print(len(emp))
        print(", ".join(f"{u}-{v}" for u, v in emp))
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
