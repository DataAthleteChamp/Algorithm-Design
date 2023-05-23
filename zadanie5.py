import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.components import connected_components


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


V = int(input("Podaj liczbę wierzchołków: "))
q = float(input("Podaj stopień wypełnienia: "))

G = generuj_graf(V, q)

for i, component in enumerate(connected_components(G), 1):
    print(f"Spójna składowa {i}: {list(component)}")

# Sprawdzamy, czy dwa wierzchołki należą do tej samej spójnej składowej
v1, v2 = map(int, input("Podaj dwa wierzchołki (oddzielone spacją): ").split())
same_component = any(
    {v1, v2}.issubset(component) for component in connected_components(G))  # dfs i struktura zbiorów rozłącznych
print(f"Wierzchołki {v1} i {v2} {'należą' if same_component else 'nie należą'} do tej samej spójnej składowej.")


nx.draw(G, with_labels=True)
plt.show()
