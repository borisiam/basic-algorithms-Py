class MaxHeap(object):


    def __init__(self,size):
        self.heapSize = int(size)
        self.heap = [0]*self.heapSize
        self.currentPosition = -1

    def insert_item(self, item):

        if self.isfull():
            print("Heap is full...")
            return False

        self.currentPosition += 1
        self.heap[self.currentPosition] = item
        self.fixup(self.currentPosition)

    def isfull(self):
        if self.currentPosition + 1 == self.heapSize:
            return True
        else:
            return False

    def fixup(self, index):
        parentIndex = int(index/2)
        currentIndex = index

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[currentIndex]:
            tmpItem = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[currentIndex]
            self.heap[currentIndex] = tmpItem
            currentIndex = parentIndex
            parentIndex = int(parentIndex/2)


    def get_max(self):
        print(self.heap[0])
        return self.heap[0]

    def heapsort(self):

        for i in range(0, self.currentPosition + 1):
            tmp = self.heap[0]
            print("%d" % tmp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = tmp
            self.fixDown(0, self.currentPosition - i - 1)

    def fixDown(self, startindex, endindex):
        for i in range(startindex, endindex):
            if self.heap[0] < self.heap[i]:
                self.fixup(i)
            else:
                continue







