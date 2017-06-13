class Stack(object):

    def __init__(self):
        self.stack = []
        self.numberOfItems = 0

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.insert(self.numberOfItems, data)
        self.numberOfItems += 1

    def pop(self):
        data = self.stack.pop()
        return data

    def peek(self):
        print(self.stack[self.numberOfItems - 1])
        return self.stack[self.numberOfItems - 1]

    def print(self):
        print(self.stack)