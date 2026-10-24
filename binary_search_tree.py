from collections import deque

# Pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            else:
                return
            
    def search(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True
            current = current.left if data < current.data else current.right
        return False

    def inorder(self, node):        # kiri -> node -> kanan
        if node:
                self.inorder(node.left)
                print(node.data, end=" ")
                self.inorder(node.right)

    def preorder(self, node):       # node -> kiri -> kanan
            if node:
                print(node.data, end=" ")
                self.preorder(node.left)
                self.preorder(node.right)

    def postorder(self, node):      # kiri -> kanan -> node
            if node:
                self.postorder(node.left)
                self.postorder(node.right)
                print(node.data, end=" ")

    def level_order(self):
        if not self.root:
            return
        antrean = deque([self.root])
        while antrean:
            node = antrean.popleft()
            print(node.data, end=" ")
            if node.left:
                antrean.append(node.left)
            if node.right:
                antrean.append(node.right)

    def min_value(self):
        current = self.root
        while current.left:         # terus ke kiri
            current = current.left
        return current.data

    def max_value(self):
        current = self.root
        while current.right:        # terus ke kanan
            current = current.right
        return current.data

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            # Kasus 1 dan 2: nol atau satu anak
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Kasus 3: dua anak
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self.delete(node.right, successor.data)
        return node

bst = BST()
for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(x)

bst.inorder(bst.root)       # 1 3 4 6 7 8 10 13 14  (terurut!)
print()
print(bst.search(6))        # True
print(bst.search(99))       # False
print(bst.min_value())      # 1
print(bst.max_value())      # 14
print(bst.height(bst.root)) # 4

bst.root = bst.delete(bst.root, 3)
bst.inorder(bst.root)       # 1 4 6 7 8 10 13 14