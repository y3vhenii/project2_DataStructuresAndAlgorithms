from graphNode import GraphNode


class GridGraph:
    def __init__(self):
        self.cells = list()

    def addGridNode(self, x, y, nodeVal):
        newNode = GraphNode(x, y, nodeVal)
        self.cells.append(newNode)

    def addUndirectedEdge(self, first, second):
        # Boolean to check whether they could be neighbors
        realNeighbors = False
        if first.x + 1 == second.x and first.y == second.y or first.x - 1 == second.x and first.y == second.y:
            realNeighbors = True
        if first.x == second.x and first.y + 1 == second.y or first.x == second.x and first.y - 1 == second.y:
            realNeighbors = True
        # If they are neighbors
        if realNeighbors:
            # Retrieve the indexes of both nodes within the list
            index1 = -1
            index2 = -1
            # Look them up in the list
            for node in self.cells:
                if node.x == first.x and node.y == first.y:
                    index1 = self.cells.index(node)
                if node.x == second.x and node.y == second.y:
                    index2 = self.cells.index(node)
            # If both nodes are in the graph
            if index1 != -1 and index2 != -1:
                self.cells[index1].neighbors.append(self.cells[index2])
                self.cells[index2].neighbors.append(self.cells[index1])

    def removeUndirectedEdge(self, first, second):
        # Retrieve the indexes of both nodes within the list
        index1 = -1
        index2 = -1
        # Look them up in the list
        for node in self.cells:
            if node.x == first.x and node.y == first.y:
                index1 = self.cells.index(node)
            if node.x == second.x and node.y == second.y:
                index2 = self.cells.index(node)
        # If both nodes are in the graph
        if index1 != -1 and index2 != -1:
            # Handles edge cases when both nodes are not connected
            try:
                self.cells[index1].neighbors.remove(self.cells[index2])
            except ValueError:
                pass
            try:
                self.cells[index2].neighbors.remove(self.cells[index1])
            except ValueError:
                pass

    def getAllNodes(self):
        return self.cells