def encontra_ciclo_euleriano(g, s):
    stack = []
    ciclo = []
    arestas = set(g.arestas)
    vizinhos = {v: list(g.vizinhos(v)) for v in g.vertices}
    v = s

    while len(stack) > 0 or len(vizinhos[v]) > 0:
        print(f"Visitando: {v}, vizinhos: {vizinhos[v]}")
        print(f"Arestas restantes: {len(arestas)}")

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
