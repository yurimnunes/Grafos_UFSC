from Grafo_Dirigido import Grafo
def ordenacao_topologica(grafo):
    visitados = set()
    ordem = []
    visitando = set()
    ciclo_detectado = False

    def dfs(u):
        nonlocal ciclo_detectado
        if u in visitando:
            ciclo_detectado = True
            return
        if u in visitados:
            return
        visitados.add(u)
        visitando.add(u)
        for v in grafo.vizinhos(u):
            dfs(v)
            if ciclo_detectado:
                return
        visitando.remove(u)
        ordem.append(u)

    for u in grafo.vertices:
        if u not in visitados:
            dfs(u)
            if ciclo_detectado:
                return None  # Ciclo encontrado

    return ordem[::-1]  # Inverte para obter a ordem topológica


def main():
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 ordenacao_topologica.py arquivo_grafo")
        return
    arquivo = sys.argv[1]
    try:
        grafo = Grafo(arquivo)
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return

    ordem = ordenacao_topologica(grafo)
    ordem_name = [grafo.rotulo(v) for v in ordem]
    if ordem is None:
        print("O grafo contém um ciclo, não é possível realizar a ordenação topológica.")
    else:
        print("Ordenação topológica:")
        print(" → ".join(map(str, ordem_name)))


if __name__ == "__main__":
    main()