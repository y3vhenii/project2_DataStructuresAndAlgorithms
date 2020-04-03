#
# Created by: Yevhenii Ganusich
# IMPORTANT NOTE: Please run this script using python Graph.py and NOT python3 Graph.py to avoid any compilation errors.
# The tests for all the functions are in Main
#

import math
import random
import sys


# Class for edge object
class Edge:
    def __init__(self, d, w):
        self.destination = d
        self.weight = w


# Class for Graph node object
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = list()
        self.visited = False


# Class for weighted graph object
class WeightedGraph:
    def __init__(self):
        self.vertices = list()

    # This adds a new node to the graph
    def addNode(self, nodeVal):
        newNode = GraphNode(nodeVal)
        self.vertices.append(newNode)

    # This adds weighted edge between first and second node
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

    # This removes weighted edge between first and second node
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

    # Returns all the vertices of the graph
    def getAllNodes(self):
        return self.vertices


# Helper function which takes in distances dictionary and visited set, returns node with smallest distance
def minDist(distances, visited):
    ans = None
    m = sys.maxint
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
    for k in range(0, n):
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
    for i in range(0, n):
        # If graph is empty
        if i == 0:
            newGraph.addNode(i)
        # If graph is not empty
        else:
            newGraph.addNode(i)
            # Link the previous node to the last node
            newGraph.addWeightedEdge(newGraph.vertices[i-1], newGraph.vertices[i], 1)

    return newGraph


if __name__ == "__main__":

    print("########################## DIJKSTRA'S FOR LINKED LIST TEST (Size 5) ##########################")
    # Create a linked list graph
    graph = createLinkedList(5)
    # Print out every node, its neighbors and their weights
    for vertex in graph.vertices:
        print("Current vetex: " + str(vertex.val))
        for neighbor in vertex.neighbors:
            print("Neighbor: " + str(neighbor.destination.val) + " Distance: " + str(neighbor.weight))

    # Return the dictionary with nodes and their shortest paths
    dijkstraAnswer = dijkstras(graph.vertices[0])
    # Print the results
    for key, value in dijkstraAnswer.items():
        print("The minimum distance from 0 to " + str(key.val) + " is " + str(value))

    print("########################## END OF DIJKSTRA'S FOR LINKED LIST TEST ##########################")
    print(" ")
    print("########################## DIJKSTRA'S FOR RANDOM COMPLETE GRAPH TEST (Size 4) ##########################")

    # Create a random complete weighted graph
    graph1 = createRandomCompleteWeightedGraph(5)
    # Print out every node, its neighbors and their weights
    for vertex in graph1.vertices:
        print("Current vertex: " + str(vertex.val))
        for neighbor in vertex.neighbors:
            print("Neighbor: " + str(neighbor.destination.val) + " Distance: " + str(neighbor.weight))

    # Return the dictionary with nodes and their shortest paths
    dijkstraAnswer = dijkstras(graph1.vertices[0])
    # Print the returned dictionary
    for key, value in dijkstraAnswer.items():
        print("The minimum distance from 0 to " + str(key.val) + " is " + str(value))

    print("########################## END OF DIJKSTRA'S FOR RANDOM COMPLETE GRAPH TEST ##########################")

