import random, sys
from weightedGraph import WeightedGraph


# Helper function which takes in distances dictionary and visited set, returns node with smallest distance
def minDist(distances, visited):
    ans = None
    m = sys.maxsize
    for curr in distances.keys():
        if curr not in visited and distances[curr] <= m:
            m = distances[curr]
            ans = curr
    return ans


# Returns a dictionary mapping each Node node in the graph to the minimum value from start to get to node
def dijkstras(start):
    # Instantiate distances dictionary
    distances = {}
    # Set the distance for the origin to 0.
    distances[start] = 0
    # Visited set
    visited = set()
    # Set curr equal to start
    curr = start

    # While curr is not empty and not equal to infinity
    while curr is not None:
        # Finalize curr
        visited.add(curr)
        # Iterate over its neighbors
        for neighbor in curr.neighbors:
            # If the neighbor is not in the distances dictionary yet
            if neighbor.destination not in distances or distances[neighbor.destination] > distances[curr] + neighbor.weight:
                distances[neighbor.destination] = distances[curr] + neighbor.weight
        # Look for next node that is unvisited and has the smallest distance
        curr = minDist(distances, visited)

    return distances


# Creates random weighted graph
def createRandomCompleteWeightedGraph(n):
    # Create and populate the graph
    newGraph = WeightedGraph()
    for k in range(n):
        newGraph.addNode(k)

    # Create edges between all the nodes in the graph
    for currIndex in range(len(newGraph.vertices)):
        for secondaryIndex in range(len(newGraph.vertices)):
            if currIndex != secondaryIndex:
                newGraph.addWeightedEdge(newGraph.vertices[currIndex], newGraph.vertices[secondaryIndex], random.randint(1, 100))

    return newGraph


# This function creates a linked list graph of size n
def createLinkedList(n):
    newGraph = WeightedGraph()
    for i in range(n):
        newGraph.addNode(i)
        # If graph is not empty
        if i != 0:
            # Link the previous node to the last node
            newGraph.addWeightedEdge(newGraph.vertices[i-1], newGraph.vertices[i], 1)
    return newGraph


def printGraph(graph):
    # Print out every node, its neighbors and their weights
    for vertex in graph.vertices:
        print("Current vetex: " + str(vertex.val))
        for neighbor in vertex.neighbors:
            print("Neighbor: " + str(neighbor.destination.val) + " Distance: " + str(neighbor.weight))
    print(" ")


def printDijkstras(dict):
    # Print the results
    for key, value in dict.items():
        print("The minimum distance from 0 to " + str(key.val) + " is " + str(value))
    print(" ")


if __name__ == "__main__":

    print("########################## DIJKSTRA'S FOR LINKED LIST TEST (Size 5) ##########################")
    # Create a linked list graph
    graph = createLinkedList(5)
    printGraph(graph)
    # Return the dictionary with shortest paths and print
    dijkstraAnswer = dijkstras(graph.vertices[0])
    printDijkstras(dijkstraAnswer)
    print("##################### DIJKSTRA'S FOR RANDOM COMPLETE GRAPH TEST (Size 5) ###################")
    # Create a random complete weighted graph
    graph1 = createRandomCompleteWeightedGraph(5)
    printGraph(graph1)
    # Return the dictionary with shortest paths and print
    dijkstraAnswer = dijkstras(graph1.vertices[0])
    printDijkstras(dijkstraAnswer)
