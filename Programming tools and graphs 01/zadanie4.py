import networkx as nx
import matplotlib.pyplot as plt
import random

n = int(input("Podaj liczbę wierzchołków: "))

G = nx.Graph()

pos = {}
for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    #losowanie wspolrzednych z rozkladu jednostajnego
    pos[i] = (x, y)
    G.add_node(i)
#tworze wierzcholki

for i in range(n):
    for j in range(i+1, n):
        if random.random() < 0.5: #zeby sie za duzo krawedzi nie potworzylo( z prawdopodobienstwem 0.5)
            G.add_edge(i, j)
#tworze krawedzie

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

plt.axis("off")
plt.show()
