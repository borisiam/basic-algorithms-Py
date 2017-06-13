
class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.node = None

class Node(object):

    def __init__(self, height, nodeId, parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode

class Edge(object):

    def __init__(self, weight, startVertex, tergetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = tergetVertex


    def __cmp__(self, oterEdge):
         return self.cmp(self.weight, oterEdge.weight)

    def __lt__(self, otherEdge):
        selfPriority = self.weight
        otherPriority = otherEdge.weight
        return selfPriority < otherPriority

class DisjointSet(object):

    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)

    def find(self, node):

        # Finding a root (representative of a set)
        currentNode = node

        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode

        # Flattening a tree, to achieve an O(1) complexity on a lookup
        root = currentNode
        currentNode = node

        while currentNode is not root:
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp

    def merge(self, node1, node2):

        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return "Nodes are in the same set"

        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        if root1.height < root2.height:
            root1.parentNode = root2
        if root1.height > root2.height:
            root2.parentNode = root1
        else:
            root2.parentNode = root1
            root1.height = root1.height +1

    def create_sets(self, vertexList):
        for v in vertexList:
            self.make_set(v)

    def make_set(self, vertex):
        node = Node(0,len(self.rootNodes),None)
        vertex.node = node
        self.rootNodes.append(node)
        self.setCount += 1
        self.nodeCount += 1


class KruskalAlgorithm(object):

    def __init__(self, vertexList, edgeList):
        self.vertexList = vertexList
        self.edgeList = edgeList

        disjointSet = DisjointSet(vertexList)
        spanningTree = []

        edgeList.sort()

        for edge in edgeList:

             u = edge.startVertex
             v = edge.targetVertex

             if disjointSet.find(u.node) is not disjointSet.find(v.node):
                 spanningTree.append(edge)
                 disjointSet.merge(u.node, v.node)

             for edge in spanningTree:
                 print(edge.startVertex.name," - ", edge.targetVertex.name)


