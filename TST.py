
class Node(object):

    def __init__(self, character):
        self.char = character
        self.leftNode = None
        self.rightNode = None
        self.middleNode = None
        self.value = 0


class TST(object):

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value, 0)

    def put_item(self, node, key, value, index):

        c = key[index]

        if node is None:
            node = Node(c)

        if c < node.char:
            node.leftNode = self.put_item(node.leftNode, key, value, index)

        elif c > node.char:
            node.rightNode = self.put_item(node.rightNode, key, value, index)

        elif index < len(key) -1:
            node.middleNode = self.put_item(node.middleNode, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.get_item(self.root, key, 0)

        if node is None:
            return -1

        return node.value

    def get_item(self, node, key, index):

        if node is None:
            return None

        c = key[index]

        if c < node.char:
            return self.get_item(node.leftNode, key, index)
        if c > node.char:
            return self.get_item(node.rightNode, key, index)
        elif index < len(key) -1:
            return self.get_item(node.middleNode, key, index+1)
        else:
            print(node.value)
            return node
