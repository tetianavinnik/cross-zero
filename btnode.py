"""BTNode"""

class BTNode():
    """Class for node representation"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.points = 0
        self.position = None