import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #tworze pusty graf
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)    #weight koszt przejscia z wierzcholka na drugi
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
#dodaje krawędzie wraz z wagami

pos = nx.spring_layout(G) #tworze układ wierzcholkow z freamworka networkx
#spring_layout sposob rzmieszczenia wierzcholkow te ktore sie lacza blisko siebie te bez polaczen dalej

nx.draw_networkx_nodes(G, pos, node_size = 500) #rysuje wierzcholki grafu
#node_size wielkosc wierzcholkow domyslnie 300
nx.draw_networkx_labels(G, pos) #dodaje etykiety wierzchołkowe
nx.draw_networkx_edges(G, pos) #rysuje krawędzie grafu
plt.show()
