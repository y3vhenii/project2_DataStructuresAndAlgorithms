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
        # Let the function know that its a global variable and make it empty first in case its not empty
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
