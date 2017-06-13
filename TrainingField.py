from BFSP import Vertex, Edge, BFSP

n1 = Vertex("node1")
n2 = Vertex("node2")
n3 = Vertex("node3")
n4 = Vertex("node4")
n5 = Vertex("node5")
n6 = Vertex("node6")

e1 = Edge(10, n1, n4)
e2 = Edge(5, n4, n3)
e3 = Edge(7, n1, n3)
e4 = Edge(2, n1, n2)
e5 = Edge(3, n2, n5)
e6 = Edge(1, n5, n3)

n1.adjList.append(e1)
n1.adjList.append(e3)
n4.adjList.append(e2)
n1.adjList.append(e4)
n2.adjList.append(e5)
n5.adjList.append(e6)

edgeList = [e1,e2,e3,e4,e5,e6]
nodeList = [n1,n2,n3,n4,n5,n6]


dsp = BFSP()

dsp.calc_shortest_path(nodeList, edgeList, n1)
dsp.get_shortest_path(n3)
