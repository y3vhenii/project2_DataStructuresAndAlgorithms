from graphNode import GraphNode
from graphEdge import Edge


class WeightedGraph:
    def __init__(self):
        self.vertices = list()

    def addNode(self, nodeVal):
        newNode = GraphNode(nodeVal)
        self.vertices.append(newNode)

    def addWeightedEdge(self, first, second, weight):
        # Retrieve the indexes of both nodes within the list
        index1 = -1
        index2 = -1
        # Look them up in the list
        for node in self.vertices:
            if node.val == first.val:
                index1 = self.vertices.index(node)
            if node.val == second.val:
                index2 = self.vertices.index(node)

        # If both nodes are in the graph
        if index1 != -1 and index2 != -1:
            # Instantiate an edge and add it to first nodes neighbors
            newWeightedEdge = Edge(self.vertices[index2], weight)
            self.vertices[index1].neighbors.append(newWeightedEdge)

    def removeDirectedEdge(self, first, second):
        # Retrieve the indexes of both nodes within the list
        index1 = -1
        index2 = -1
        # Look them up in the list and see if they exist
        for node in self.vertices:
            if node.val == first.val:
                index1 = self.vertices.index(node)
            if node.val == second.val:
                index2 = self.vertices.index(node)

        # If both nodes are in the graph
        if index1 != -1 and index2 != -1:
            # Remove the weighted edge from first's neighbors
            for edge in range(len(self.vertices[index1].neighbors)):
                if self.vertices[index1].neighbors[edge].destination.val == self.vertices[index2].val:
                    self.vertices[index1].neighbors.remove(self.vertices[index1].neighbors[edge])
                    break

    def getAllNodes(self):
        return self.vertices
