import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generuj_graf(V, q):
    max_edges = V * (V - 1) // 2
    E = int(q * max_edges)
    G = nx.DiGraph()
    G.add_nodes_from(range(V))
    while G.number_of_edges() < E:
        v1, v2 = np.random.choice(V, 2, replace=False)
        if not G.has_edge(v1, v2) and v1 != v2:
            G.add_edge(v1, v2)
    return G


def dfs(graph, visited, stack, node, pos):
    visited.add(node)
    for neighbour in graph.neighbors(node):
        if neighbour not in visited:
            dfs(graph, visited, stack, neighbour, pos)
    stack.append(node)
    colors = ['r' if node == x or x in stack else 'b' for x in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_color=colors, node_size=800)
    plt.show()


def topological_sort(graph):
    visited = set()
    stack = []
    pos = nx.spring_layout(graph)
    for node in list(graph):
        if node not in visited:
            dfs(graph, visited, stack, node, pos)
    stack.reverse()
    return stack


def print_graph(graph):
    print("Wierzchołki: ", end="")
    for node in graph.nodes:
        print(node, end=" ")
    print("\nKrawędzie: ")
    for edge in graph.edges:
        print(edge)


def main():
    V = int(input("Podaj liczbę wierzchołków: "))
    q = float(input("Podaj stopień wypełnienia: "))
    filename = 'graph.txt'

    while True:
        G = generuj_graf(V, q)
        nx.write_adjlist(G, filename)
        G = nx.read_adjlist(filename, create_using=nx.DiGraph())

        if nx.is_directed_acyclic_graph(G):
            print('graf DAG:')
            print_graph(G)
            break
        else:
            print("Wygenerowany graf nie jest DAG. Zły graf:")
            print_graph(G)

    sorted_nodes = topological_sort(G)
    print("Wierzchołki posortowane topologicznie:", sorted_nodes)


if __name__ == "__main__":
    main()


# Sortowanie topologiczne DAG=(skierowanego grafu acyklicznego) – liniowe uporządkowanie wierzchołków,
# w którym jeśli istnieje krawędź skierowana prowadząca od wierzchołka
# x do y to x znajdzie się przed wierzchołkiem y
