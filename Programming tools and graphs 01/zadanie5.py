import networkx as nx
import matplotlib.pyplot as plt
import random

n = int(input("Podaj liczbę wierzchołków: "))
G = nx.Graph()

pos = {}
iter_count = 0

for i in range(n):
    # losowanie pozycji środka okręgu
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)

    # sprawdzenie, czy okrag nie zachodzi na istniejace już okregi
    while any((x - pos[j][0]) ** 2 + (y - pos[j][1]) ** 2 < 4 ** 2 for j in range(i)):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        iter_count += 1
        # przerwanie pętli, jeśli nie udało się dodać nowego okręgu w ciągu 100 iteracji
        if iter_count > 100:
            break
    if iter_count <= 100:
        pos[i] = (x, y)
        G.add_node(i)

for i in range(n):
    for j in range(i + 1, n):
        if (pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2 < 0.2 ** 2:
            G.add_edge(i, j)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

# wyświetlenie ponumerowanych okręgów
for i, p in pos.items():
    plt.text(p[0], p[1], str(i + 1), ha='center', va='center') #zeby etykiety byly na srodku wierzcholkow

plt.show()
