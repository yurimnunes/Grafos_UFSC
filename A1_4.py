def bellman_ford(g, s, w):
    dist = []
    pred = []

    for v in range(g.qtdVertices() + 1):
        dist.append(float("inf"))
        pred.append(None)
    dist[s] = 0

    i = 1
    while i < g.qtdVertices():
        for u, v in g.arestas:
            if dist[u] + w[u - 1][v - 1] < dist[v]:
                dist[v] = dist[u] + w[u - 1][v - 1]
                pred[v] = u
        i += 1

    for u, v in g.arestas:
        if dist[u] + w[u - 1][v - 1] < dist[v]:
            print("Tem ciclo negativo.")

    for v in g.vertices:
        pred_list = []
        if dist[v] != float("inf"):
            u = v
            while u is not None:
                pred_list.insert(0, u)
                u = pred[u]
        lista_str = ",".join(map(str, pred_list))
        print(f"{v}: {lista_str}; d= {dist[v]}")
