import networkx as nx
import matplotlib.pyplot as plt
import json
import random
from typing import List, Tuple
from networkx.drawing.nx_agraph import graphviz_layout


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node(key={self.key}, value={self.value})"


class RobotBST:
    def __init__(self):
        self.root = None
        self.key_attr = None
        self.graph = nx.DiGraph()

    def set_key_attr(self, key_attr):
        self.key_attr = key_attr

    def add_robot(self, robot, node_attr='robot'):
        key = robot[self.key_attr]
        if self.root is None:
            self.root = Node(key, robot)
            self.graph.add_node(str(key), **{node_attr: robot})
        else:
            self._add(self.root, key, robot, node_attr)

    def _add(self, node, key, robot, node_attr):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, robot)
                self.graph.add_node(str(key), **{node_attr: robot})
                self.graph.add_edge(str(node.key), str(key))
            else:
                self._add(node.left, key, robot, node_attr)
        else:
            if node.right is None:
                node.right = Node(key, robot)
                self.graph.add_node(str(key), **{node_attr: robot})
                self.graph.add_edge(str(node.key), str(key))
            else:
                self._add(node.right, key, robot, node_attr)

    def search_robot(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def remove_robot(self, key):
        self.root, removed_node = self._remove(self.root, key)
        if removed_node:
            self.graph.remove_node(str(removed_node.key))
        return removed_node

    def _remove(self, node, key):
        if node is None:
            return node, None
        if key < node.key:
            node.left, removed_node = self._remove(node.left, key)
        elif key > node.key:
            node.right, removed_node = self._remove(node.right, key)
        else:
            removed_node = node
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right, _ = self._remove(node.right, temp.key)
        return node, removed_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def draw_tree(self):
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        plt.show()

    def save_tree(self, filename):
        with open(filename, 'w') as f:
            json.dump(dict(self.graph.nodes(data=True)), f)

    def load_tree(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for key, attr in data.items():
            self.add_robot(attr['robot'])

    def left_rotation(self, key):
        node = self._search(self.root, key)
        if node:
            new_root = self._left_rotate(node)
            if node == self.root:
                self.root = new_root

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.left = x
        return y

    def right_rotation(self, key):
        node = self._search(self.root, key)
        if node:
            new_root = self._right_rotate(node)
            if node == self.root:
                self.root = new_root

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.right = x
        return y


def generuj_robota() -> Tuple[str, float, int, int]:
    typy = ["AGV", "AFV", "ASV", "AUV"]
    typ = random.choice(typy)
    cena = round(random.uniform(0, 10000), 2)
    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)
    return typ, cena, zasieg, kamera


def generuj_liste_robotow(n: int) -> List[Tuple[str, float, int, int]]:
    return [generuj_robota() for _ in range(n)]


def wyswietl_roboty(roboty: List[Tuple[str, float, int, int]]):
    print("TYP   CENA       ZASIEG     KAMERA")
    for robot in roboty:
        print(f"{robot[0]:<5} {robot[1]:<9.2f} {robot[2]:<9} {robot[3]}")


def zapisz_roboty_do_pliku(roboty: List[Tuple[str, float, int, int]], nazwa_pliku: str):
    with open(nazwa_pliku, "w") as plik:
        for robot in roboty:
            plik.write(f"{robot[0]} {robot[1]} {robot[2]} {robot[3]}\n")


def odczytaj_roboty_z_pliku(nazwa_pliku: str) -> List[Tuple[str, float, int, int]]:
    roboty = []
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            typ, cena, zasieg, kamera = linia.strip().split()
            roboty.append((typ, float(cena), int(zasieg), int(kamera)))
    return roboty


roboty = generuj_liste_robotow(50)
zapisz_roboty_do_pliku(roboty, "roboty.txt")
roboty_z_pliku = odczytaj_roboty_z_pliku("roboty.txt")
wyswietl_roboty(roboty_z_pliku)

bst = RobotBST()
key_attr = input("Podaj cechę robota, która będzie kluczem w drzewie (indeks, typ, cena, zasieg, kamera): ")
bst.set_key_attr(key_attr)
for i, robot in enumerate(roboty):
    bst.add_robot({'indeks': i, 'typ': robot[0], 'cena': robot[1], 'zasieg': robot[2], 'kamera': robot[3]})
bst.draw_tree()
bst.save_tree('drzewo.json')

# usun = int(input("co usunąć: "))  # indeks zasieg kamera
# usun = str(input("co usunąć: ")) #typ
#usun = float(input("co usunąć: "))  # cena
#bst.remove_robot(usun)
bst.save_tree('drzewo.json')
#bst.draw_tree()

bst.load_tree('drzewo.json')
# wyszukaj = int(input("co wyszukać: "))  # indeks zasieg kamera
# wyszukaj = str(input("co wyszukać: ")) #typ
#wyszukaj = float(input("co wyszukać: "))  # cena
#print(bst.search_robot(wyszukaj))


def inorder(node):
    if node:
        inorder(node.left)
        print(f"Visiting node: {node}")
        # bst.draw_tree()  # Wyświetlanie drzewa po odwiedzeniu węzła
        inorder(node.right)


def preorder(node):
    if node:
        print(f"Visiting node: {node}")
        # bst.draw_tree()  # Wyświetlanie drzewa przed rekurencyjnym wywołaniem
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(f"Visiting node: {node}")
        # bst.draw_tree()  # Wyświetlanie drzewa po odwiedzeniu węzła


# print("Inorder Traversal:")
# inorder(bst.root)
# print('------------------------------------------------------')
# print("\nPreorder Traversal:")
# preorder(bst.root)
# print('------------------------------------------------------')
# print("\nPostorder Traversal:")
# postorder(bst.root)


rotate_key = float(input("Podaj klucz węzła do rotacji: "))
rotate_direction = input("Podaj kierunek rotacji (left/right): ")

if rotate_direction == "left":
    bst.left_rotation(rotate_key)
elif rotate_direction == "right":
    bst.right_rotation(rotate_key)

bst.draw_tree()


"""
Rotacja w prawo jest operacją, w której węzeł staje się prawym dzieckiem swojego lewego dziecka. 
Rotacja w prawo jest używana, gdy lewe poddrzewo jest cięższe lub dłuższe od prawego poddrzewa. 
Rotacja w prawo pomaga przywrócić równowagę drzewa.

Rotacja w lewo jest operacją, w której węzeł staje się lewym dzieckiem swojego prawego dziecka. 
Rotacja w lewo jest używana, gdy prawe poddrzewo jest cięższe lub dłuższe od lewego poddrzewa. 
Rotacja w lewo również pomaga przywrócić równowagę drzewa.

"""