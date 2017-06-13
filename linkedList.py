class Node(object):

    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self, data):
        self.size +=1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def insert_node_end(self, data):

        if self.head:
            current_node = self.head
            self.size += 1
            new_node = Node(data)

            while current_node.next_node is not None:
                current_node = current_node.next_node

            current_node.next_node = new_node

        else:
            self.insert_node(data)

    def remove_nodes_data(self, data):

        if not self.head:
            return "Linked list is empty"

        else:
            current_node = self.head

            while current_node is not None:
                print("s1")
                if current_node.data == data:

                    if current_node.next_node is not None:
                        print("s3")
                        current_node.next_node.previous_node = current_node.previous_node
                        print("s4")
                        if current_node is not self.head:
                            print("s5")
                            current_node.previous_node.next_node = current_node.next_node
                    else:
                        current_node.previous_node.next_node = None

                current_node = current_node.next_node
        while self.head.data == data:
            self.head = self.head.next_node

    def remove_node_data(self, data):

        if not self.head:
            return
        else:
            current_node = self.head
            prev_node = None

            while current_node.data != data:
                prev_node = current_node
                current_node = current_node.next_node

            if prev_node is None:
                self.head = current_node.next_node
                self.head.previous_node = None
            else:
                prev_node.next_node = current_node.next_node


    def print_nodes(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next_node

        print(nodes)




