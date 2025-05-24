from A1_1 import Grafo

def kruskal(grafo):
    arestas_nao_dirigidas = set()
    for a, b in grafo.arestas:
        if a < b:
            arestas_nao_dirigidas.add((a, b, grafo.peso(a, b)))
        else:
            arestas_nao_dirigidas.add((b, a, grafo.peso(a, b)))
    arestas_ordenadas = sorted(arestas_nao_dirigidas, key=lambda x: x[2])

    pai = {v: v for v in grafo.vertices}

    def find(u):
        while pai[u] != u:
            pai[u] = pai[pai[u]]  # Compressão de caminho
            u = pai[u]
        return u

    def union(u, v):
        raiz_u = find(u)
        raiz_v = find(v)
        if raiz_u != raiz_v:
            pai[raiz_v] = raiz_u

    agm = []
    soma_pesos = 0.0

    for a, b, peso in arestas_ordenadas:
        if find(a) != find(b):
            union(a, b)
            agm.append((a, b))
            soma_pesos += peso
        if len(agm) == grafo.qtdVertices() - 1:
            break

    # Verifica se o grafo é conectado
    if len(agm) != grafo.qtdVertices() - 1:
        return None, None  # Grafo desconectado
    
    return soma_pesos, agm

def main():
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 kruskal.py arquivo_grafo")
        return
    arquivo = sys.argv[1]
    try:
        grafo = Grafo(arquivo)
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return

    soma_pesos, arestas_agm = kruskal(grafo)
    if soma_pesos is None:
        print("O grafo não é conectado. Não existe árvore geradora mínima.")
    else:
        print(f"{soma_pesos:.1f}")
        print(", ".join([f"{a}-{b}" for a, b in arestas_agm]))

if __name__ == "__main__":
    main()