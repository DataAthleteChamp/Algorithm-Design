import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


def draw_path(graph, path, flow, step):
    plt.figure()  # Tworzenie nowego okna
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=path, edge_color='r', width=2.0)
    edge_labels = {(u, v): f"{flow[(u, v)]}/{C[u][v]}" for u, v in graph.edges()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(f"Step {step}")
    plt.draw()


def max_flow(C, s, t):
    n = len(C)
    F = np.zeros_like(C)
    path = bfs(C, F, s, t)
    step = 1
    draw_path(G, [], F, step)
    plt.pause(2)  # Pauza
    while path is not None:
        step += 1
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        draw_path(G, path, F, step)
        plt.pause(2)  # Pauza
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


num_nodes = int(input("Podaj liczbę wierzchołków: "))
fill = float(input("Podaj stopień wypełnienia: "))

G = nx.DiGraph()
G.add_nodes_from(range(num_nodes))
C = np.zeros((num_nodes, num_nodes))
num_edges = int((num_nodes * (num_nodes - 1) * fill))

edges_added = 0
while edges_added < num_edges:
    u = random.randint(0, num_nodes - 1)
    v = random.randint(0, num_nodes - 1)
    if u != v and C[u][v] == 0:
        G.add_edge(u, v)
        C[u][v] = random.randint(1, 10)
        edges_added += 1

pos = nx.spring_layout(G)
plt.figure()  # Tworzenie nowego okna
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500)
plt.title("Initial Graph")
plt.show()

source = int(input("Podaj wierzchołek źródłowy: "))
sink = int(input("Podaj wierzchołek docelowy: "))

if not G.has_node(source) or not G.has_node(sink):
    print("Podane wierzchołki nie istnieją w grafie.")
else:
    max_flow_value = max_flow(C, source, sink)

    print("Edmonds-Karp algorithm")
    print("max Flow value:", max_flow_value)

plt.show()