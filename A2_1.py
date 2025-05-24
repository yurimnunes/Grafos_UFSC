
from Grafo_Dirigido import Grafo
def kosaraju(graph):
    visited = set()
    order = []

    def dfs_post_order(start):
        stack = [(start, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, True))
            for neighbor in reversed(graph.vizinhos(node)):
                if neighbor not in visited:
                    stack.append((neighbor, False))

    for v in graph.vertices:
        if v not in visited:
            dfs_post_order(v)

    order.reverse()

    predecessores = {v: [] for v in graph.vertices}
    for a, b in graph.arestas:
        predecessores[b].append(a)

    visited = set()
    cfc = []
    for v in order:
        if v not in visited:
            component = []
            stack = [v]
            visited.add(v)
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in predecessores[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            cfc.append(sorted(component))
    
    return sorted(cfc, key=lambda x: x[0])


def main():
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 A1_1.py arquivo_grafo")
        return
    arquivo = sys.argv[1]
    grafo = Grafo(arquivo)
    componentes = kosaraju(grafo)
    for componente in componentes:
        print(", ".join(map(str, componente)))


if __name__ == "__main__":
    main()