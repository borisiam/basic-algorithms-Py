import sys
import heapq

class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):

        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class Vertex(object):

    def __init__(self, name):

        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjList = []
        self.minDist = sys.maxsize

    def __cmp__(self, otherVertex):
        return self.cmp(self.minDist, otherVertex.minDist)

    def __lt__(self, other):
        selfPriority = self.minDist
        otherPriority = other.minDist
        return selfPriority < otherPriority

class DSP(object):

    def calc_shortest_path(self, startVertex):

        q = []
        startVertex.minDist = 0
        heapq.heappush(q, startVertex)

        while len(q) > 0:

            actualVertex = heapq.heappop(q)

            for edge in actualVertex.adjList:
                u = edge.startVertex
                v = edge.targetVertex
                newDist = u.minDist + edge.weight

                if newDist < v.minDist:
                    v.predecessor = u
                    v.minDist = newDist
                    heapq.heappush(q, v)

    def get_shortest_path(self, targetVertex):
        print("Shortest path to", targetVertex.name, "takes", targetVertex.minDist, "units")

        node = targetVertex

        while node is not None:
            print(node.name)
            node = node.predecessor


