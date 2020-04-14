import collections


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
        return topMDFS

    # Helper function for mDFS
    def mDfsHelper(self, node, stack):
        node.visited = True

        # For all of the node's neighbors
        for neighbor in node.neighbors:
            if not neighbor.visited:
                # If the neighbor isn't visited, call mDfsHelper
                self.mDfsHelper(neighbor, stack)
        # After calling modifiedDfsHelper on ALL neighbors, add the original node to the output stack.
        stack.append(node)

