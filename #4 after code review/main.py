import random
from directedGraph import DirectedGraph
from topSort import TopSort


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
        neighborNodeIndex1 = random.randint(node.val, len(newGraph.vertices) - 1)
        neighborNodeIndex2 = random.randint(node.val, len(newGraph.vertices) - 1)
        # If number generated is not being used yet and it doesn't represent node.val
        if node.val != neighborNodeIndex1 and neighborNodeIndex1 not in randomVertices:
            newGraph.addDirectedEdge(newGraph.vertices[node.val], newGraph.vertices[neighborNodeIndex1])
            randomVertices.add(neighborNodeIndex1)
        # If second number generated is not being used yet and it doesn't represent node.val
        if node.val != neighborNodeIndex2 and neighborNodeIndex2 not in randomVertices:
            newGraph.addDirectedEdge(newGraph.vertices[node.val], newGraph.vertices[neighborNodeIndex2])
            randomVertices.add(neighborNodeIndex2)

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
