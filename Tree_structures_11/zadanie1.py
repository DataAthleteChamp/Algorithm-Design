import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def to_dict(self):
        return {
            "key": self.key,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, key, parent_key=None):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_node_recursive(key, parent_key, self.root)

    def _add_node_recursive(self, key, parent_key, node):
        if node is None:
            return Node(key)
        if node.key == parent_key:
            if node.left is None:
                node.left = Node(key)
            elif node.right is None:
                node.right = Node(key)
        else:
            if node.left is not None:
                self._add_node_recursive(key, parent_key, node.left)
            if node.right is not None:
                self._add_node_recursive(key, parent_key, node.right)

    def delete_node(self, key):
        if self.root is not None:
            self.root = self._delete_node_recursive(self.root, key)

    def _delete_node_recursive(self, node: Node, key):
        if node is None:
            return None
        if node.key == key:
            return None
        node.left = self._delete_node_recursive(node.left, key)
        node.right = self._delete_node_recursive(node.right, key)
        return node

    def show_tree(self):
        def _traverse_nodes(node):
            if node is not None:
                nodes.append(node.key)
                _traverse_nodes(node.left)
                _traverse_nodes(node.right)

        def _traverse_edges(node):
            if node is not None:
                if node.left is not None:
                    edges.append((node.key, node.left.key))
                if node.right is not None:
                    edges.append((node.key, node.right.key))
                _traverse_edges(node.left)
                _traverse_edges(node.right)

        nodes = []
        edges = []
        _traverse_nodes(self.root)
        _traverse_edges(self.root)

        graph = nx.Graph()
        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)
        pos = graphviz_layout(graph, prog='dot')

        nx.draw(graph, pos, with_labels=True, arrows=False)
        plt.show()

    def save_tree(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.root.to_dict(), file)

    def load_tree(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self.root = self._load_node_recursive(data)

    def _load_node_recursive(self, data):
        if data is None:
            return None
        node = Node(data['key'])
        node.left = self._load_node_recursive(data['left'])
        node.right = self._load_node_recursive(data['right'])
        return node


def main():
    tree = BinaryTree()

    # Initialize tree
    tree.add_node('A')  # Root node
    tree.add_node('B', 'A')
    tree.add_node('C', 'A')
    tree.add_node('D', 'B')
    tree.add_node('E', 'B')
    tree.add_node('F', 'C')
    tree.add_node('G', 'C')

    while True:
        print("1. Add node")
        print("2. Delete node")
        print("3. Display tree")
        print("4. Save tree to file")
        print("5. Load tree from file")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            key = input("Enter node key: ")
            parent_key = input("Enter parent node key (if none, it will be added as root): ")
            tree.add_node(key, parent_key)

        elif choice == '2':
            key = input("Enter key of the node to delete: ")
            tree.delete_node(key)

        elif choice == '3':
            tree.show_tree()

        elif choice == '4':
            filename = 'drzewo.json'
            tree.save_tree(filename)

        elif choice == '5':
            filename = 'drzewo.json'
            tree.load_tree(filename)

        elif choice == '6':
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
