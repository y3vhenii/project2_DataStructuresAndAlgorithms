import random
from graph import Graph
from graphNode import GraphNode
from graphSearch import GraphSearch


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


def printGraph(graph):
    if graph is not None:
        for every in graph.vertices:
            print("Current node is: " + str(every.val))
            print("Current node's neighbors are:")
            print(",".join(str(child.val) for child in every.neighbors))
            print(" ")
    print(" ")


def printTraversal(traversal):
    if traversal is not None:
        print(",".join(str(every.val) for every in traversal))
        print(" ")
    else:
        print("EMPTY")
        print(" ")


if __name__ == "__main__":
    print("########################## START OF TEST FOR 3B ##########################")
    randomGraph = createRandomUnweightedGraphIter(25)
    printGraph(randomGraph)
    print("########################## START OF TEST FOR 3C ##########################")
    linkedList = createLinkedList(25)
    printGraph(linkedList)
    print("######################## START OF TEST FOR 3D, 3E ########################")
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    d = GraphNode('D')
    e = GraphNode('E')
    f = GraphNode('F')  # Unconnected node
    a.neighbors = [b, c]
    b.neighbors = [d, e, a]
    c.neighbors = [a]
    d.neighbors = [b]
    e.neighbors = [b]
    path = GraphSearch()
    dfsRec = path.DFSRec(a, e)
    dfsIter = path.DFSIter(a, e)
    print("Recursive DFS Traversal is: ")
    printTraversal(dfsRec)
    print("Iterative DFS Traversal is: ")
    printTraversal(dfsIter)

    print("######################## START OF TEST FOR 3F, 3G ########################")
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
    print("Recursive BFT Traversal is: ")
    printTraversal(bftRec)
    print("Iterative BFT Traversal is: ")
    printTraversal(bftIter)

    print("######################## START OF TEST FOR 3H, 3I ########################")
    # My computer does not crash due to stack overflow for 100 elements. Anything above it will cause stack overflow.
    bigLinkedList = createLinkedList(100)
    print("Created big Linked List...")
    recursiveReturn = BFTRecLinkedList(bigLinkedList)
    print("Finished recursive BFT...")
    iterativeReturn = BFTIterLinkedList(bigLinkedList)
    print("Finished iterative BFT...")
    print("Recursive Linked-List BFT Traversal is: ")
    printTraversal(recursiveReturn)
    print("Iterative Linked-List BFT Traversal is: ")
    printTraversal(iterativeReturn)
