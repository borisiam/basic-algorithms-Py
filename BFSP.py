import sys


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjList = []
        self.minDist = sys.maxsize


class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class BFSP(object):

    HAS_CYCLE = False

    def calc_shortest_path(self,vertexList, edgeList, startVertex):

        startVertex.minDist = 0

        for i in range (0, len(vertexList) - 1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex

                newDist = u.minDist + edge.weight

                if newDist < v.minDist:
                    v.minDist = newDist
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected")
                self.HAS_CYCLE = True
                return

    def hasCycle(self, edge):
        if (edge.startVertex.minDist + edge.weight) < edge.startVertex.minDist:
            return True
        else:
            return False

    def get_shortest_path(self, targetVertex):

        if not self.HAS_CYCLE:
            print("Shortest path exists, value:", targetVertex.minDist)

            node = targetVertex

            while node is not None:
                print(node.name)
                node = node.predecessor
