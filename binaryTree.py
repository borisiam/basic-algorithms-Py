class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):
    traversedData = []
    foundNode = None
    fdata = None

    def __init__(self):
        self.root = None


    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        print(node.data)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        print(node.data)
        return node.data

    def traverse_in_order(self):
        if self.root:
            self.in_order_traverse(self.root)
            tempTraversedData = self.traversedData
            self.traversedData = []
            print(tempTraversedData)
            return tempTraversedData

    def in_order_traverse(self, node):
        if node.leftChild:
            self.in_order_traverse(node.leftChild)

        self.traversedData.append(node.data)

        if node.rightChild:
            self.in_order_traverse(node.rightChild)

    def traverse_pre_order(self):
        if self.root:
            self.pre_order_traverse(self.root)
            tempTraversedData = self.traversedData
            self.traversedData = []
            print(tempTraversedData)
            return tempTraversedData

    def pre_order_traverse(self, node):
        self.traversedData.append(node.data)
        if node.leftChild:
            self.pre_order_traverse(node.leftChild)
        if node.rightChild:
            self.pre_order_traverse(node.rightChild)

    def traverse_post_order(self):
        if self.root:
            self.post_order_traverse(self.root)
            tempTraversedData = self.traversedData
            self.traversedData = []
            print(tempTraversedData)
            return tempTraversedData

    def post_order_traverse(self, node):
        if node.leftChild:
            self.post_order_traverse(node.leftChild)
        if node.rightChild:
            self.post_order_traverse(node.rightChild)
        self.traversedData.append(node.data)

    def find_node(self, data):
        self.fdata = data
        if self.root:
            self.node_find(self.root)

        print(self.foundNode.data)
        self.fdata = None
        return self.foundNode

    def node_find(self, node):
        if node.data > self.fdata:
            self.node_find(node.leftChild)
        if node.data < self.fdata:
            self.node_find(node.rightChild)
        else:
            self.foundNode = node

    def delete_node(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.leftChild = self.delete_node(data, node.leftChild)
        if data > node.data:
            node.rightChild = self.delete_node(data, node.rightChild)
        if data == node.data:
            if not node.leftChild and not node.rightChild:
                print("Deleting a leaf node...")
                del node
                return None

            if not node.leftChild:
                print("Deleting node with a single right child...")
                tmpNode = node.rightChild
                del node
                return tmpNode

            if not node.rightChild:
                print("Deleting node with a single left child...")
                tmpNode = node.leftChild
                del node
                return tmpNode

            print("Deleting node with both children")
            tempNode = self.get_predecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.delete_node(tempNode.data, node.leftChild)

        return node

    def get_predecessor(self, node):
        if node.rightChild:
            self.get_predecessor(node.rightChild)

        return node












