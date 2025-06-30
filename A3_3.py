import sys
from itertools import combinations
from A1_1 import Grafo


def is_independent_set(grafo, conjunto):
    for u in conjunto:
        for v in conjunto:
            if u != v and v in grafo.vizinhos(u):
                return False
    return True


def gerar_subconjuntos(vertices):
    n = len(vertices)
    for i in range(1, 2**n):
        conjunto = [vertices[j] for j in range(n) if (i & (1 << j))]
        yield conjunto


def lawler_coloring(grafo):
    n = grafo.qtdVertices()
    V = tuple(grafo.vertices)
    dp = {(): (0, {})}

    for i in range(1, 2**n):
        subconj = tuple(V[j] for j in range(n) if (i >> j) & 1)
        min_color = float("inf")
        best_coloring = {}

        for conjunto_indep in gerar_subconjuntos(subconj):
            if not is_independent_set(grafo, conjunto_indep):
                continue

            restante = tuple(v for v in subconj if v not in conjunto_indep)
            if restante not in dp:
                continue

            cor_antes, coloracao_antes = dp[restante]
            nova_coloracao = coloracao_antes.copy()
            for v in conjunto_indep:
                nova_coloracao[v] = cor_antes + 1

            if cor_antes + 1 < min_color:
                min_color = cor_antes + 1
                best_coloring = nova_coloracao

        dp[subconj] = (min_color, best_coloring)

    final = dp[V]
    return final[0], final[1]


def executar_coloring(input_file):
    grafo = Grafo(input_file)
    num_cores, coloracao = lawler_coloring(grafo)

    print(num_cores)
    resultado = [str(coloracao[v]) for v in sorted(grafo.vertices)]
    print(", ".join(resultado))


def main():
    if len(sys.argv) != 2:
        print("Uso A3_3 (Coloração): python3 A3_3.py <nome_arquivo>")
        sys.exit(1)

    try:
        executar_coloring(sys.argv[1])
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
