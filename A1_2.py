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
    # Para consulta é mais rapido
    marked = [False for i in range(n_nodes + 1)]
    visitados = []
    fila = []
    fila.append(origem)
    marked[origem] = True
    visitados.append(origem)
    i = 0
    print(f"{i}: {origem}")
    while len(fila) != 0:
        u = fila.pop(0)
        temp = ""
        for v in grafo.vizinhos(u):
            # temp+= str(v) + ','
            if marked[v] == False:
                marked[v] = True
                visitados.append(v)
                fila.append(v)
                temp += str(v) + ","
        if len(temp) != 0:
            i += 1
            print(f"{i}: {temp[:-1]}")
    return visitados


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
