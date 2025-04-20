# quero que esse codigo receba outros parametros quando for chamado no terminal

import sys
from A1_1 import Grafo

# DESCOMENTAR NA ENTREGA
# python A1_2.py arquivo origem
# if len(sys.argv) != 3:
#    print('Uso: python A1_2.py arquivo_path nó_origem')
#    exit(1)
# grafo = Grafo(sys.argv[1])
# origem = int(sys.argv[2])


def BFS(grafo: Grafo, origem: int):
    n_nodes = grafo.qtdVertices()
    marked = [False for _ in range(n_nodes + 1)]
    fila = [[origem]]  # Cada elemento da fila representa um nível
    marked[origem] = True
    nivel = 0

    while fila:
        vertices_nivel = fila.pop(0)
        if not vertices_nivel:  # Nível vazio, encerra
            break
        # Formata e imprime o nível atual (acho q funciona)
        print(f"{nivel}: {', '.join(map(str, vertices_nivel))}")
        # Coleta os vértices do próximo nível
        proximo_nivel = []
        for u in vertices_nivel:
            for v in grafo.vizinhos(u):
                if not marked[v]:
                    marked[v] = True
                    proximo_nivel.append(v)
        # se houver vertices adiciona proximo nivel
        if proximo_nivel:
            fila.append(proximo_nivel)
            nivel += 1


def main():
    if len(sys.argv) != 3:
        print("Uso A1_2 (BFS): python3 A1_2.py <nome_arquivo> <vertice_inicial>")
        sys.exit(1)

    grafo_nome = sys.argv[1]
    v = int(sys.argv[2])
    g = Grafo(grafo_nome)
    BFS(g, v)


if __name__ == "__main__":
    main()
