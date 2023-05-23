import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def generuj_graf(V, q):
    max_edges = V * (V - 1) // 2

    #rzeczywista liczbę krawędzi
    E = int(q * max_edges)
    G = nx.Graph()

    G.add_nodes_from(range(V))

    edges = set()
    while G.number_of_edges() < E:
        v1, v2 = np.random.choice(V, 2, replace=False)
        if not G.has_edge(v1, v2):
            G.add_edge(v1, v2)

    adjacency_matrix = nx.adjacency_matrix(G).toarray()
    incidence_matrix = nx.incidence_matrix(G, oriented=True).toarray()
    return G, adjacency_matrix, incidence_matrix


V = int(input("Podaj liczbę wierzchołków: "))
q = float(input("Podaj stopień wypełnienia: "))

G, adjacency_matrix, incidence_matrix = generuj_graf(V, q)

print("Macierz sąsiedztwa:")
print(adjacency_matrix)
print("Rozmiar macierzy sąsiedztwa:", adjacency_matrix.shape)
#sasiad liczba wierzchołkow x liczba wierzchołkow z czym się łączą

print("Macierz incydencji:")
print(incidence_matrix.astype(int))
#print(incidence_matrix)
print("Rozmiar macierzy incydencji:", incidence_matrix.shape)
#incydencja liczba wierzchołkow x liczb krawędzi
nx.draw(G, with_labels=True)
plt.show()