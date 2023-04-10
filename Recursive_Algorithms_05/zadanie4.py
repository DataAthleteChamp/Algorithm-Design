import networkx as nx


def min_sciezka(G, u, v, visited=None): # u pocz, v kon
    if visited is None:
        visited = {} #słownik
    if u == v:
        return 0
    visited[u] = True
    min_path = float('inf') # dlugosc sciezki niekonczonosc
    for neighbor in G[u]:
        if neighbor not in visited:
            path = 1 + min_sciezka(G, neighbor, v, visited) #rekurencja
            if path < min_path:
                min_path = path
    visited[u] = False
    return min_path


G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2),(1,2), (1, 3), (2, 4), (4, 5)])

u = int(input('podaj wierchołek startowy:'))
v = int(input('podaj wierchołek końcowy:'))
path_length = min_sciezka(G, u, v)
print(f"Minimalna długość ścieżki między wierzchołkami {u} i {v}: {path_length}")


#zlozonosc O(liczba krawedzi w grafie)