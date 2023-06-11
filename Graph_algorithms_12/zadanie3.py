import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


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


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal_algorithm(G):
    result = []
    edges = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))

    parent = {}
    rank = {}

    for node in G.nodes():
        parent[node] = node
        rank[node] = 0

    for edge in edges:
        u, v, _ = edge
        root1 = find(parent, u)
        root2 = find(parent, v)
        if root1 != root2:
            result.append(edge)
            union(parent, rank, root1, root2)

    return nx.Graph(result)


def visualize(G, MST):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=MST.edges(), edge_color='r', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.savefig('kruskal')
    plt.show()


def kruskal_algorithm_visualized(G):
    edges = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))

    parent = {}
    rank = {}

    MST = nx.Graph()

    for node in G.nodes():
        parent[node] = node
        rank[node] = 0

    for edge in edges:
        u, v, w = edge
        root1 = find(parent, u)
        root2 = find(parent, v)
        if root1 != root2:
            MST.add_edge(u, v, weight=w['weight'])  # Dodajemy wagę krawędzi do MST
            visualize(G, MST)
            union(parent, rank, root1, root2)

    print("Posortowane krawędzie MST:")
    sorted_edges = sorted(MST.edges(data=True), key=lambda t: t[2].get('weight', 1))
    for u, v, wt in sorted_edges:
        print(f"({u}, {v}, {wt['weight']})")


def main():
    V = int(input("Podaj liczbę wierzchołków: "))
    q = float(input("Podaj stopień wypełnienia: "))

    G = generuj_graf(V, q)
    write_graph_to_file(G, "graf.txt")

    G = read_graph_from_file("graf.txt")
    kruskal_algorithm_visualized(G)


if __name__ == "__main__":
    main()

"""
Minimalne drzewo rozpinające (MST), znane również jako minimalne drzewo spinające, 
to podzbiór krawędzi grafu nieskierowanego, połączonych tak, 
aby tworzyły drzewo obejmujące wszystkie wierzchołki, 
przy czym suma wag wszystkich krawędzi w drzewie jest minimalna.

Algorytm Kruskala zaczyna od sortowania wszystkich krawędzi od najmniejszej do największej. 
Następnie dodaje krawędzie do drzewa w kolejności od najmniejszej do największej, 
o ile dodanie krawędzi nie stworzy cyklu.

"""
