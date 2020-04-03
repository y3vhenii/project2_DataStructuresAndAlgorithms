#
# Created by: Yevhenii Ganusich
# IMPORTANT NOTE: Please run this script using python Graph.py and NOT python3 Graph.py to avoid any compilation errors.
# The tests for all the functions are in Main
#

import random
import collections


class GraphNode:
    def __init__(self, val):
        self.val = val
        # Neighbors at index 0 would contain adjacent top node and index 1 would contain adjacent right node
        self.neighbors = list()
        self.visited = False


class DirectedGraph:
    def __init__(self):
        self.vertices = list()

    # This adds a new node to the graph
    def addNode(self, nodeVal):
        newNode = GraphNode(nodeVal)
        self.vertices.append(newNode)

    # This adds directed edge between first and second node
    def addDirectedEdge(self, firstNode, secondNode):
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

    # This removes undirected edge between first and second
    def removeDirectedEdge(self, firstNode, secondNode):
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

    # This returns a set of all nodes in the graph
    def getAllNodes(self):
        return self.vertices


class TopSort:
    def __init__(self):
        pass

    # Using Kahn's topological sort on the graph
    def Kahns(self, graph):
        # This list will keep the graph in a topologically sorted order
        tSort = list()
        # Create a map that will store in-degrees for every vertex
        inDegree = dict()
        # Initialize in-degree hash-map with all 0s
        for node in graph.vertices:
            inDegree[node] = 0

        # Populate hash-map with the current numbers of incoming edges
        for node in graph.vertices:
            for neighbor in node.neighbors:
                inDegree[neighbor] = inDegree[neighbor] + 1

        # Instantiate a queue
        queue = collections.deque()

        # Populate the queue with nodes that have in-degree of 0
        for curr in list(inDegree.keys())[::-1]:
            if inDegree[curr] == 0:
                queue.append(curr)
                inDegree[curr] = inDegree[curr] - 1

        while queue:
            # Retrieve current element in the queue
            curr = queue.popleft()
            # Append it to the return list
            tSort.append(curr)

            # Reduce in-degree of every neighbor by 1
            for neighbor in curr.neighbors:
                inDegree[neighbor] = inDegree[neighbor] - 1

            # Populate the queue with nodes that have in-degree of 0
            for curr in list(inDegree.keys())[::-1]:
                if inDegree[curr] == 0:
                    queue.append(curr)
                    inDegree[curr] = inDegree[curr] - 1

        return tSort

    # Using mDFS topological sort on the graph
    def mDFS(self, graph):
        stack = list()

        # For all nodes in graph, if it's not visited, call modifiedDfsHelper
        for node in graph.vertices:
            if not node.visited:
                self.mDfsHelper(node, stack)

        # Output everything in the stack in order.
        topMDFS = reversed(stack)
        # s = "Output of modified dfs: "
        # while stack:
        #    currNode = stack.pop()
        #    s += "->" + str(currNode.val)
        # print(s)
        return topMDFS

    # Helper function for mDFS
    def mDfsHelper(self, node, stack):
        # TODO set the node as visited
        node.visited = True

        # For all of the node's neighbors
        for neighbor in node.neighbors:
            if not neighbor.visited:
                # If the neighbor isn't visited, call mDfsHelper
                self.mDfsHelper(neighbor, stack)
        # After calling modifiedDfsHelper on ALL neighbors, add the original node to the output stack.
        stack.append(node)

# This function generates random DAG of size n
def createRandomDAGIter(n):
    newGraph = DirectedGraph()
    # Create n nodes
    for k in range(0, n):
        newGraph.addNode(k)

    # Assign each node 2 random vertices (might assign 0, 1 or 2 vertices)
    for node in newGraph.vertices:
        randomVertices = set()
        # Generate 2 random numbers which will represent direction up and right
        neighborNode1 = random.randint(node.val, len(newGraph.vertices) - 1)
        neighborNode2 = random.randint(node.val, len(newGraph.vertices) - 1)
        # If number generated is not being used yet and it doesn't represent node.val
        if node.val != neighborNode1 and neighborNode1 not in randomVertices:
            newGraph.addDirectedEdge(newGraph.vertices[node.val], newGraph.vertices[neighborNode1])
            randomVertices.add(neighborNode1)
        # If second number generated is not being used yet and it doesn't represent node.val
        if node.val != neighborNode2 and neighborNode2 not in randomVertices:
            newGraph.addDirectedEdge(newGraph.vertices[node.val], newGraph.vertices[neighborNode2])
            randomVertices.add(neighborNode2)

    return newGraph



if __name__ == "__main__":
    # Create random DAG with 1000 nodes
    randomGraph = createRandomDAGIter(1000)
    if randomGraph is not None:
        for every in randomGraph.vertices:
            print("Current node is: " + str(every.val))
            print("Current node is adjacent to : " + ",".join(str(child.val) for child in every.neighbors))
            print("-------------------------------------------------------")

    # Kahn's topological sort
    topologicalSort = TopSort()
    kahnsTopSort = topologicalSort.Kahns(randomGraph)
    print("Kahns topological sort: ")
    print(",".join(str(every1.val) for every1 in kahnsTopSort))

    # mDFS topological sort
    secondSort = TopSort()
    mdfstopsort = secondSort.mDFS(randomGraph)
    print("mDFS topological sort: ")
    print(",".join(str(every1.val) for every1 in mdfstopsort))