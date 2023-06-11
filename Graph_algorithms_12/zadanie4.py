import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generuj_graf(V, q):
    max_edges = V * (V - 1) // 2
    E = int(q * max_edges)
    G = nx.Graph()
    G.add_nodes_from(range(V))
    while G.number_of_edges() < E:
        v1, v2 = np.random.choice(V, 2, replace=False)
        if not G.has_edge(v1, v2) and v1 != v2:
            G.add_edge(v1, v2, weight=np.random.randint(1, 10))
    return G


def write_graph_to_file(G, filename):
    nx.write_weighted_edgelist(G, filename)


def read_graph_from_file(filename):
    return nx.read_weighted_edgelist(filename, create_using=nx.Graph(), nodetype=int)


def get_path(predecessor, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    return path


def visualize_step(G, d, node_color, pos):
    plt.figure()
    nx.draw(G, pos, node_color=node_color, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    print("Aktualne odległości:", d)
    plt.show()


def dijkstra(G, source):
    pos = nx.spring_layout(G)
    node_color = ['blue' if node == source else 'grey' for node in G.nodes]

    d = {node: np.inf for node in G.nodes}
    d[source] = 0
    predecessor = {node: None for node in G.nodes}
    Q = list(G.nodes)

    visualize_step(G, d, node_color, pos)

    while Q:
        u = min(Q, key=lambda node: d[node])
        Q.remove(u)

        for i, node in enumerate(G.nodes):
            if node == u:
                node_color[i] = 'green'
            elif d[node] != np.inf and node_color[i] != 'green':
                node_color[i] = 'blue'

        for v in G.neighbors(u):
            alt = d[u] + G[u][v]['weight']
            if alt < d[v]:
                d[v] = alt
                predecessor[v] = u

        visualize_step(G, d, node_color, pos)

    return d, predecessor


def main():
    V = int(input("Podaj liczbę wierzchołków: "))
    q = float(input("Podaj stopień wypełnienia: "))

    G = generuj_graf(V, q)
    write_graph_to_file(G, 'graph.txt')

    G = read_graph_from_file('graph.txt')

    start = int(input("Podaj wierzchołek początkowy: "))
    end = int(input("Podaj wierzchołek końcowy: "))

    distances, predecessors = dijkstra(G, start)
    path = get_path(predecessors, start, end)

    print("Droga wynosi:", distances[end])
    print("Ścieżka:", path)


if __name__ == "__main__":
    main()



"""

Algorytm Dijkstry działa iteracyjnie, realizując pewne kroki za każdym razem, kiedy przetwarza nowy wierzchołek. 
Procedura jest następująca:
Na początku każdej iteracji, wierzchołek u z najmniejszą wartością odległości (zaczynając od źródła) 
jest wybierany spośród niewykorzystanych wierzchołków. Wierzchołek ten jest następnie oznaczany jako "przetworzony" 
i usuwany z listy niewykorzystanych wierzchołków.

Następnie, dla każdego sąsiada v wierzchołka u, obliczana jest alternatywna ścieżka do v poprzez u. 
Jeżeli ta alternatywna ścieżka jest krótsza od dotychczas znanej ścieżki do v, 
to aktualizowana jest odległość d[v] oraz v jest ustawiane jako następca u w najkrótszej ścieżce.

Krok pierwszy jest powtarzany, dopóki wszystkie wierzchołki nie zostaną przetworzone.

Kod zaproponowany wcześniej uwzględnia kroki wyświetlania stanu algorytmu po każdej iteracji. W każdym kroku, 
algorytm wypisuje aktualne odległości do wierzchołków i rysuje graf, pokazując wierzchołki, 
które zostały już przetworzone (na zielono), wierzchołki, które zostały odkryte, 
ale jeszcze nie przetworzone (na niebiesko), oraz wierzchołki, które nie zostały jeszcze odkryte (na szaro).

"""