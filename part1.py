import random
#
# Created by: Yevhenii Ganusich
# IMPORTANT NOTE: Please run this script using python Graph.py and NOT python3 Graph.py to avoid any compilation errors.
# The tests for all the functions are in Main
#

# Global variable to store path of recursive DFS (for DFSRec only)
recursiveDfsPath = []
recursiveDfsSuccess = False
# Global variable to store path of recursive BFT (for BFTRec only)
recursiveBftPath = []
discovered = []


class GraphSearch:
    def __init__(self):
        pass

    # Recursively returns list of nodes in Depth-First search order
    def DFSRec(self, start, end):
        # Let the function know that its a global variable and make it empty first
        global recursiveDfsPath
        global recursiveDfsSuccess
        recursiveDfsPath = []
        # Let the function populate the recursiveDfsPath
        self.DFSRecHelper(start, end)
        if not recursiveDfsSuccess:
            return None
        else:
            return recursiveDfsPath

    # Helper function for DFSRec
    def DFSRecHelper(self, start, end):
        global recursiveDfsPath
        global recursiveDfsSuccess
        # If the current node is the node we're looking for
        if start == end:
            recursiveDfsPath.append(start)
            recursiveDfsSuccess = True
            return
        # Continue looking
        if start not in recursiveDfsPath and not recursiveDfsSuccess:
            recursiveDfsPath.append(start)
            for neighbor in start.neighbors:
                # Recursion happens here
                self.DFSRecHelper(neighbor, end)

    # Iteratively returns list of nodes in Depth-First search order
    def DFSIter(self, start, end):
        # Path traversed
        traversal = []
        # Search successful
        success = False
        # Initiate a stack
        stack = [start]
        while len(stack) > 0:
            # Pop the element from the stack
            currentNode = stack.pop()
            # Mark currentNode as visited
            traversal.append(currentNode)
            # If current node is what we are looking for, terminate the search
            if currentNode == end:
                success = True
                break
            # Otherwise...
            else:
                for neighbor in currentNode.neighbors:
                    # If the neighbor is not visited, push it on the stack
                    if neighbor not in traversal:
                        stack.append(neighbor)
        # Final check
        if success:
            return traversal
        else:
            return None

    # Recursively returns the traversal of the Graph in Breadth-First traversal order
    def BFTRec(self, graph):
        global recursiveBftPath
        global discovered
        # Clear the path just in case the variable was used multiple times throughout the runtime
        recursiveBftPath = []
        queue =[]
        # Let the function populate the recursiveBftPath
        for i in range(0, len(graph.vertices)):
            if graph.vertices[i] not in discovered:
                discovered.append(graph.vertices[i])
                queue.append(graph.vertices[i])
                # Call recursive helper function here
                self.BFTRecHelper(graph, queue)
        return recursiveBftPath

    # Helper function for BFTRec
    def BFTRecHelper(self, graph, queue):
        global recursiveBftPath
        global discovered
        # If queue is empty
        if len(queue) == 0:
            return
        # Pop front element from the queue and append it to the traversal list
        currentNode = queue.pop(0)
        recursiveBftPath.append(currentNode)
        # Go through every neighbor of current node
        for neighbor in currentNode.neighbors:
            # And check if it was discovered yet, if not, add to discovered list and append to queue
            if neighbor not in discovered:
                discovered.append(neighbor)
                queue.append(neighbor)
        # Recursion happens here
        self.BFTRecHelper(graph, queue)

    # Iteratively returns the traversal of the Graph in Breadth-First traversal order
    def BFTIter(self, graph):
        iterTraversed = []
        iterDiscovered = []
        for i in range(0, len(graph.vertices)):
            if graph.vertices[i] not in iterDiscovered:
                queue = []
                iterDiscovered.append(graph.vertices[i])
                queue.append(graph.vertices[i])
                while len(queue) > 0:
                    curr = queue.pop(0)
                    iterTraversed.append(curr)
                    for neighbor in curr.neighbors:
                        if neighbor not in iterDiscovered:
                            iterDiscovered.append(neighbor)
                            queue.append(neighbor)
        return iterTraversed


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = list()
        self.visited = False


class Graph:
    def __init__(self):
        self.vertices = list()

    # This adds a new node to the graph
    def addNode(self, nodeVal):
        newNode = GraphNode(nodeVal)
        self.vertices.append(newNode)

    # This adds undirected edge between first and second node
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

    # This removes undirected edge between first and second
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

    # This returns a set of all nodes in the graph
    def getAllNodes(self):
        return self.vertices


# This function creates random nodes with random vertices
def createRandomUnweightedGraphIter(n):
    newGraph = Graph()
    # Create n nodes
    for k in range(0, n):
        randomItem = k
        newGraph.addNode(randomItem)

    # Assign each node random vertices
    for node in newGraph.vertices:
        randomVertecies = set()
        # Store current index
        currentIndex = newGraph.vertices.index(node)
        # Generate random number of neighbors amount from current size of the graph
        neighborNodes = random.randint(0, len(newGraph.vertices)-1)
        # Iterate neighborNodes times
        for i in range(0, neighborNodes):
            # Get random index within the vertices
            randomVertex = random.randint(0, len(newGraph.vertices)-1)
            # Check whether the randomVertex is not current node and whether it was assigned to the node before
            # The fact that this statement will not execute sometimes makes it even more random
            if randomVertex != currentIndex and randomVertex not in randomVertecies:
                newGraph.vertices[currentIndex].neighbors.append(newGraph.vertices[randomVertex])
                randomVertecies.add(randomVertex)

    return newGraph

# This function creates a linked list graph of size n
def createLinkedList(n):
    newGraph = Graph()
    for i in range(0, n):
        # If graph is empty
        if i == 0:
            newGraph.addNode(i)
        # If graph is not empty
        else:
            newGraph.addNode(i)
            # Link the previous node to the last node
            newGraph.vertices[i-1].neighbors.append(newGraph.vertices[i])
    return newGraph

# This should run BFT recursively on a LinkedList
def BFTRecLinkedList(graph):
    recursivePath = GraphSearch()
    recPath = recursivePath.BFTRec(graph)
    return recPath


# This should run BFT iteratively on a LinkedList
def BFTIterLinkedList(graph):
    iterativePath = GraphSearch()
    iterPath = iterativePath.BFTIter(graph)
    return iterPath


if __name__ == "__main__":
    #################################################################################
    # To test 3b (createRandomUnweightedGraphIter)
    print("########################## START OF TEST FOR 3B ##########################")
    randomGraph = createRandomUnweightedGraphIter(25)
    if randomGraph is not None:
        for every in randomGraph.vertices:
            print("Current node is: " + str(every.val))
            print("Current node's neighbors are:")
            print(",".join(str(child.val) for child in every.neighbors))
    print("########################### END OF TEST FOR 3B ###########################")
    print(" ")
    print("########################## START OF TEST FOR 3C ##########################")
    linkedList = createLinkedList(25)
    if linkedList is not None:
        for every in linkedList.vertices:
            print("Current node is: " + str(every.val))
            print("Current node's neighbors are:")
            print(",".join(str(child.val) for child in every.neighbors))
    print("########################### END OF TEST FOR 3C ###########################")
    print(" ")
    print("########################## START OF TEST FOR 3D, 3E ##########################")
    # Instantiate nodes
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    d = GraphNode('D')
    e = GraphNode('E')
    f = GraphNode('F')  # Unconnected node
    # Assign neighbors to nodes
    a.neighbors = [b, c]
    b.neighbors = [d, e, a]
    c.neighbors = [a]
    d.neighbors = [b]
    e.neighbors = [b]
    # Perform the search
    path = GraphSearch()
    dfsRec = path.DFSRec(a, e)
    dfsIter = path.DFSIter(a, e)
    # If everything is found
    if dfsRec is not None and dfsIter is not None:
        # Print the traversal of the path
        print("Recursive DFS Traversal is: ")
        print(",".join(str(every.val) for every in dfsRec))
        print("Iterative DFS Traversal is: ")
        print(",".join(str(every1.val) for every1 in dfsIter))

    print("########################## END OF TEST FOR 3D, 3E ##########################")
    print(" ")
    print("########################## START OF TEST FOR 3F, 3G ##########################")
    graph = Graph()
    g = GraphNode('G')
    graph.addNode(g.val)
    h = GraphNode('H')
    graph.addNode(h.val)
    i = GraphNode('I')
    graph.addNode(i.val)
    j = GraphNode('J')
    graph.addNode(j.val)
    k = GraphNode('K')
    graph.addNode(k.val)
    l = GraphNode('L')
    graph.addNode(l.val)
    graph.addUndirectedEdge(g, h)
    graph.addUndirectedEdge(g, i)
    graph.addUndirectedEdge(h, l)
    graph.addUndirectedEdge(i, j)
    graph.addUndirectedEdge(i, k)
    path = GraphSearch()
    bftRec = path.BFTRec(graph)     # Recursive BFT
    bftIter = path.BFTIter(graph)   # Iterative BFT
    if bftRec is not None and bftIter is not None:
        # Print the traversal of the path
        print("Recursive BFT Traversal is: ")
        print(",".join(str(every.val) for every in bftRec))
        print("Iterative BFT Traversal is: ")
        print(",".join(str(every1.val) for every1 in bftIter))

    print("########################## END OF TEST FOR 3F, 3G ##########################")
    print(" ")
    print("########################## START OF TEST FOR 3H, 3I ##########################")
    # My computer works for 100 but not for 1000 or 10000 (4bg of ram)
    bigLinkedList = createLinkedList(10000)
    print("Created big Linked List")
    recursiveReturn = BFTRecLinkedList(bigLinkedList)
    print("Finished recursive BFT")
    iterativeReturn = BFTIterLinkedList(bigLinkedList)
    print("Finished iterative BFT")
    if recursiveReturn is not None and iterativeReturn is not None:
        print("Recursive Linked-List BFT Traversal is: ")
        print(",".join(str(every.val) for every in recursiveReturn))
        print("Iterative Linked-List BFT Traversal is: ")
        print(",".join(str(every.val) for every in iterativeReturn))

    print("########################## END OF TEST FOR 3H, 3I ##########################")