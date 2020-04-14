from graphNode import GraphNode


class Graph:
    def __init__(self):
        self.vertices = list()

    def addNode(self, nodeVal):
        newNode = GraphNode(nodeVal)
        self.vertices.append(newNode)

    def addUndirectedEdge(self, firstNode, secondNode):
        # Retrieve the indexes of both nodes within the list
        index1 = -1
        index2 = -1
        # Look them up in the list
        for node in self.vertices:
            if node.val == firstNode.val:
                index1 = self.vertices.index(node)
            if node.val == secondNode.val:
                index2 = self.vertices.index(node)

        # If both nodes are in the graph
        if index1 != -1 and index2 != -1:
            self.vertices[index1].neighbors.append(self.vertices[index2])
            self.vertices[index2].neighbors.append(self.vertices[index1])

    def removeUndirectedEdge(self, firstNode, secondNode):
        # Retrieve the indexes of both nodes within the list
        index1 = -1
        index2 = -1
        # Look them up in the list
        for node in self.vertices:
            if node.val == firstNode.val:
                index1 = self.vertices.index(node)
            if node.val == secondNode.val:
                index2 = self.vertices.index(node)

        # If both nodes are in the graph
        if index1 != -1 and index2 != -1:
            self.vertices[index1].neighbors.remove(self.vertices[index2])
            self.vertices[index2].neighbors.remove(self.vertices[index1])

    def getAllNodes(self):
        return self.vertices