class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjList = []
        self.visited = False
        self.predescessor = None

class BreathFirstSearch(object):

    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            actualNode = queue[0]
            for node in actualNode.adjList:
                if not node.visited:
                    queue.append(node)

            print(actualNode.name)
            queue.remove(actualNode)


class DepthFirstSearch(object):

    def dfs(self, startNode):

        startNode.visited = True
        print(startNode.name)

        for n in startNode.adjList:
            if not n.visited:

                self.dfs(n)
