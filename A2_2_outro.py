from Grafo_Dirigido import Grafo
def ordenacao_topologica_dfs(grafo):
    # Inicializações conforme Algoritmo 20
    C = {v: False for v in grafo.vertices}  # Visitado (C_v)
    T = {v: float('inf') for v in grafo.vertices}  # Tempo de descoberta
    F = {v: float('inf') for v in grafo.vertices}  # Tempo de término
    tempo = 0
    O = []  # Lista de ordenação topológica
    ciclo_detectado = [False]  # Usamos lista para permitir modificação em escopo interno

    def dfs_visit_ot(v):
        nonlocal tempo
        if C[v]:
            return
        if T[v] != float('inf') and F[v] == float('inf'):
            # Detectou um ciclo (vértice sendo revisitado durante a mesma DFS)
            ciclo_detectado[0] = True
            return

        C[v] = True
        tempo += 1
        T[v] = tempo

        # Visita todos os vizinhos (Algoritmo 21, linha 4)
        for u in grafo.vizinhos(v):
            if not C[u]:
                dfs_visit_ot(u)
            elif F[u] == float('inf'):
                # Vizinho ainda não finalizado → ciclo
                ciclo_detectado[0] = True

        tempo += 1
        F[v] = tempo
        O.insert(0, v)  # Adiciona no início (Algoritmo 21, linha 9)

    # Executa DFS para cada vértice não visitado (Algoritmo 20, linha 6-8)
    for v in grafo.vertices:
        if not C[v]:
            dfs_visit_ot(v)
            if ciclo_detectado[0]:
                return None  # Aborta se ciclo

    return O  # Ordenação topológica

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

    ordem = ordenacao_topologica_dfs(grafo)
    ordem_name = [grafo.rotulo(v) for v in ordem]
    if ordem is None:
        print("O grafo contém um ciclo. Ordenação topológica impossível.")
    else:
        print("Ordenação topológica:")
        print(" → ".join(map(str, ordem_name)))

if __name__ == "__main__":
    main()