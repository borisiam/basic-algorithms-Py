
class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVLTree(object):
    traversedData = []

    def __init__(self):
        self.root = None

    def calculate_height(self, node):
        if not node:
            return -1
        else:
            node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild))+1
            return max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild))+1


    def calcBalance(self, node):
        """
        If returns < 0, a tree is heavier on the right side
        If returns > 0, a tree is heavier on the left side
        :param node:
        :return: integer
        """
        if not node:
            return 0

        return self.calculate_height(node.leftChild) - self.calculate_height(node.rightChild)

    def rotateRight(self, node):
        print("Rotating right on the node", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = self.calculate_height(node)
        tempLeftChild.height = self.calculate_height(tempLeftChild)

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating left on the node", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = self.calculate_height(node)
        tempRightChild.height = self.calculate_height(tempRightChild)

        return tempRightChild

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            print("inserted", data)
            return Node(data)

        if data < node.data:
            print("node to left", node.data)
            node.leftChild = self.insert_node(data, node.leftChild)
        else:
            print("node to right", node.data)
            node.rightChild = self.insert_node(data, node.rightChild)

        node.height = self.calculate_height(node)
        balance = self.calcBalance(node)
        while balance < -1 or balance > 1:
            tmpnode = self.settle_violation(data, node)
            print("checking balance")
            print(tmpnode.data)
            balance = self.calcBalance(tmpnode)
            node = tmpnode
        print("balance is good on", node.data)
        return node

    def settle_violation(self, data, node):

        balance = self.calcBalance(node)

        if balance < -1 and not node.rightChild.leftChild:
             print("Rotating left")
             node = self.rotateLeft(node)
             print("returning-settled-node", node.data)
             return node

        if balance > 1 and not node.leftChild.rightChild:
             print("Rotating right")
             node = self.rotateRight(node)
             print("returning-settled-node", node.data)
             return node

        if balance > 1 and node.leftChild and data > node.leftChild.data:
             print("left-right heavy")
             node.leftChild = self.rotateLeft(node.leftChild)
             return self.rotateRight(node)

        if balance < -1 and node.rightChild and data < node.rightChild.data:
            print("Right-left heavy")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

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

    def get_min(self):
        if self.root:
            return self.min_get(self.root)

    def min_get(self, node):
        if node.leftChild:
            return self.min_get(node.leftChild)
        return node

    def get_max(self):
        if self.root:
            return self.max_get(self.root)

    def max_get(self, node):
        if node.rightChild:
            return self.max_get(node.rightChild)
        return node


    def remove_node(self, data):
        self.root = self.node_remove(self.root, data)

    def node_remove(self, node, data):

        print("im at node", node.data, "using", data)

        if data > node.data:
            node.rightChild = self.node_remove(node.rightChild, data)

        if data < node.data:
            node.leftChild = self.node_remove(node.leftChild, data)

        if data == node.data:

            if node.leftChild and node.rightChild:
                print("Deleting a parent node with both children", node.data)
                tmpNode = self.max_get(node.leftChild)
                node.data = tmpNode.data
                node.leftChild = self.node_remove(node.leftChild, node.data)
                return node

            if not node.leftChild and not node.rightChild:
                print("Deleting a leaf node", node.data)
                del node
                return None

            if node.leftChild:
                print("Deleting a node with a left child", node.data)
                tmpNode = node.leftChild
                del node
                return tmpNode

            if node.rightChild:
                print("Deleting a node with a right child", node.data)
                tmpNode = node.rightChild
                del node
                return tmpNode

        print("about to calculate balance on", node.data, "using", data)
        node.height = self.calculate_height(node)
        balance = self.calcBalance(node)
        while balance < -1 or balance > 1:
            tmpnode = self.settle_violation(data, node)
            print("checking balance")
            print(tmpnode.data)
            balance = self.calcBalance(tmpnode)
            node = tmpnode
        print("balance is good on", node.data)

        return node





