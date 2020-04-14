class GraphNode:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.neighbors = list()
        self.parent = None