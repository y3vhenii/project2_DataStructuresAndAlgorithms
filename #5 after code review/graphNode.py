class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = list()
        self.visited = False
