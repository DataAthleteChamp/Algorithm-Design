import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generuj_graf(V, q):
    max_edges = V * (V - 1) // 2
    E = int(q * max_edges)
    G = nx.Graph()
    G.add_nodes_from(range(V))
    edges = set()
    while G.number_of_edges() < E:
        v1, v2 = np.random.choice(V, 2, replace=False)
        if not G.has_edge(v1, v2):
            G.add_edge(v1, v2)
    return G


def DFS(G, v, visited, pos):
    visited.add(v)
    nx.draw(G, pos, with_labels=True, node_color=['red' if node == v else 'blue' for node in G.nodes()])
    plt.show(block=False)
    plt.pause(1)
    plt.clf()
    plt.savefig('DFS')

    for neighbor in G.neighbors(v):
        if neighbor not in visited:
            DFS(G, neighbor, visited, pos)


def main():
    V = int(input("Podaj liczbę wierzchołków: "))
    q = float(input("Podaj stopień wypełnienia: "))
    G = generuj_graf(V, q)
    filename = 'graph.txt'
    nx.write_adjlist(G, filename)
    G = nx.read_adjlist(filename)
    G = nx.relabel_nodes(G, {node: int(node) for node in G.nodes})
    pos = nx.spring_layout(G)
    visited = set()

    while True:
        start_node = input("Podaj wierzchołek startowy: ")
        if start_node.isdigit() and int(start_node) in G.nodes:
            start_node = int(start_node)
            break
        else:
            print("Niepoprawny numer wierzchołka. Spróbuj ponownie.")

    DFS(G, start_node, visited, pos)


if __name__ == "__main__":
    main()


#przeszukiwanie w głąb
# odwiedza jak najgłębsze możliwe wierzchołki na danej ścieżce zanim zwróci się, aby zbadać inne gałęzie