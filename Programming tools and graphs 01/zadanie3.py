import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Podaj liczbę wierzchołków: "))
G = nx.complete_graph(n) #graf pelny

pos = {}
for i in range(n):
    angle = 2*np.pi*i/n #kat pod ktorym wierzcholek ma zostac umieszczony na okregu
    pos[i] = (np.cos(angle), np.sin(angle))

labels = {}
for i in range(n):
    labels[i] = str(i+1) #zeby wierzcholki mialy etykiety zaczynajace sie od 1 a nie od 0

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)

plt.axis("off")
plt.show()
