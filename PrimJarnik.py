import heapq

class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []

    def __str__(self):
        return self.name

class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    def __cmp__(self, otherEdge):
        return self.cmp(self.weight, otherEdge.weight)

    def __lt__(self, other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority

class PrimsJarnik(object):

    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.fullCost = 0

    def calcSpanningTree(self, vertex):

        self.unvisitedList.remove(vertex)

        while self.unvisitedList:

            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)

            minEdge = heapq.heappop(self.edgeHeap)

            self.spanningTree.append(minEdge)
            print("edge is added to spanning tree % - %" % (minEdge.startVertex.name, minEdge.targetVertex.name))

            vertex = minEdge.targetVertex
            self.unvisitedList.remove(vertex)

    def get_spanning_tree(self):
        return self.spanningTree

