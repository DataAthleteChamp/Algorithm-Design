import networkx as nx
import matplotlib.pyplot as plt
import json
import random
from typing import List, Tuple
from networkx.drawing.nx_agraph import graphviz_layout


class Node:
    def __init__(self, key, value, color='RED'):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

    def __str__(self):
        return f"Node(key={self.key}, value={self.value}, color={self.color})"

class RedBlackTree:
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
            self.root.color = 'BLACK'  # Korzeń drzewa musi być czarny
            self.graph.add_node(str(key), **{node_attr: robot})
        else:
            self._add(self.root, key, robot, node_attr)

    def _add(self, node, key, robot, node_attr):
        if key < node.key:
            if node.left is None:
                new_node = Node(key, robot)
                new_node.parent = node
                node.left = new_node
                self.graph.add_node(str(key), **{node_attr: robot})
                self.graph.add_edge(str(node.key), str(key))
                self._fix_red_black_tree(new_node)  # Naprawa własności czerwono-czarnej po dodaniu węzła
            else:
                self._add(node.left, key, robot, node_attr)
        else:
            if node.right is None:
                new_node = Node(key, robot)
                new_node.parent = node
                node.right = new_node
                self.graph.add_node(str(key), **{node_attr: robot})
                self.graph.add_edge(str(node.key), str(key))
                self._fix_red_black_tree(new_node)  # Naprawa własności czerwono-czarnej po dodaniu węzła
            else:
                self._add(node.right, key, robot, node_attr)

    def _fix_red_black_tree(self, node):
        while node != self.root and node.color == 'RED' and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'RED':
                    # Przypadek 1: Wujek jest czerwony
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Przypadek 2: Wujek jest czarny, a węzeł jest prawym dzieckiem
                        node = node.parent
                        self._left_rotate(node)
                    # Przypadek 3: Wujek jest czarny, a węzeł jest lewym dzieckiem
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'RED':
                    # Przypadek 1: Wujek jest czerwony
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Przypadek 2: Wujek jest czarny, a węzeł jest lewym dzieckiem
                        node = node.parent
                        self._right_rotate(node)
                    # Przypadek 3: Wujek jest czarny, a węzeł jest prawym dzieckiem
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)

        self.root.color = 'BLACK'  # Korzeń drzewa musi być czarny

    def _left_rotate(self, x):
        y = x.right
        if y.left is not None:
            x.right = y.left
            y.left.parent = x
        else:
            x.right = None
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.right = x
        if x.parent:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y
        y.parent = x.parent
        x.parent = y

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
            if node is not None:
                self._fix_double_black(node)  # Naprawa własności czerwono-czarnej po usunięciu węzła
        return node, removed_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _fix_double_black(self, node):
        if node == self.root:
            return

        sibling = self._get_sibling(node)
        parent = node.parent

        if sibling is None:
            self._fix_double_black(parent)
        else:
            if sibling.color == 'RED':
                # Przypadek 1: Siostra jest czerwona
                parent.color = 'RED'
                sibling.color = 'BLACK'
                if sibling == parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
                self._fix_double_black(node)
            else:
                if (sibling.left and sibling.left.color == 'RED') or (sibling.right and sibling.right.color == 'RED'):
                    # Przypadek 2: Siostra jest czarna, a przynajmniej jedno dziecko jest czerwone
                    if sibling.left and sibling.left.color == 'RED':
                        if sibling == parent.left:
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            self._right_rotate(parent)
                        else:
                            sibling.left.color = parent.color
                            self._right_rotate(sibling)
                            self._left_rotate(parent)
                    else:
                        if sibling == parent.left:
                            sibling.right.color = parent.color
                            self._left_rotate(sibling)
                            self._right_rotate(parent)
                        else:
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self._left_rotate(parent)
                    parent.color = 'BLACK'
                else:
                    # Przypadek 3: Siostra i jej dzieci są czarne
                    sibling.color = 'RED'
                    if parent.color == 'BLACK':
                        self._fix_double_black(parent)
                    else:
                        parent.color = 'BLACK'

    def _get_sibling(self, node):
        if node == node.parent.left:
            return node.parent.right
        else:
            return node.parent.left

    def search_robot(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

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

    def right_rotation(self, key):
        node = self._search(self.root, key)
        if node:
            new_root = self._right_rotate(node)
            if node == self.root:
                self.root = new_root

    def verify_red_black_tree(self):
        if self._is_red_black_tree(self.root):
            print("Drzewo spełnia własność czerwono-czarną.")
        else:
            print("Drzewo nie spełnia własności czerwono-czarnej.")

    def _is_red_black_tree(self, node):
        if node is None:
            return True

        # Warunek 1: Wszystkie węzły są albo czarne, albo czerwone
        if node.color != 'RED' and node.color != 'BLACK':
            return False

        # Warunek 2: Korzeń jest czarny
        if node == self.root and node.color != 'BLACK':
            return False

        # Warunek 3: Żadne dwa czerwone węzły nie są połączone bezpośrednio
        if node.color == 'RED' and node.parent.color == 'RED':
            return False

        # Warunek 4: Wszystkie ścieżki z danego węzła do jego liści mają tę samą liczbę czarnych węzłów
        left_black_count = self._count_black_nodes(node.left)
        right_black_count = self._count_black_nodes(node.right)

        if left_black_count != right_black_count:
            return False

        return self._is_red_black_tree(node.left) and self._is_red_black_tree(node.right)

    def _count_black_nodes(self, node):
        if node is None:
            return 1

        left_black_count = self._count_black_nodes(node.left)
        right_black_count = self._count_black_nodes(node.right)

        return left_black_count + (1 if node.color == 'BLACK' else 0)


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

rbt = RedBlackTree()
key_attr = input("Podaj cechę robota, która będzie kluczem w drzewie (indeks, typ, cena, zasieg, kamera): ")
rbt.set_key_attr(key_attr)
for i, robot in enumerate(roboty):
    rbt.add_robot({'indeks': i, 'typ': robot[0], 'cena': robot[1], 'zasieg': robot[2], 'kamera': robot[3]})
rbt.draw_tree()
rbt.save_tree('drzewo.json')

rbt.verify_red_black_tree()

# Usuwanie węzła
usun = int(input("Podaj indeks węzła do usunięcia: "))
rbt.remove_robot(usun)
rbt.draw_tree()

# Wyszukiwanie węzła
wyszukaj = int(input("Podaj indeks węzła do wyszukania: "))
found_node = rbt.search_robot(wyszukaj)
if found_node:
    print("Znaleziono węzeł:", found_node)
else:
    print("Nie znaleziono węzła o podanym indeksie.")

# Rotacja
# rotate_key = float(input("Podaj klucz węzła do rotacji: "))
# rotate_direction = input("Podaj kierunek rotacji (left/right): ")
#
# if rotate_direction == "left":
#     rbt.left_rotation(rotate_key)
# elif rotate_direction == "right":
#     rbt.right_rotation(rotate_key)

# rbt.draw_tree()

# Weryfikacja własności czerwono-czarnej
rbt.verify_red_black_tree()
