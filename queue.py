class Queue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            print(item)
            return item
        else:
            return False

    def peek(self):
        print(self.queue[0])
        return self.queue[0]

    def print(self):
        print(self.queue)