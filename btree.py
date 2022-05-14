"""Binary Tree"""
from btnode import BTNode

class BTree:
    """Class for binary tree representation"""
    def __init__(self) -> None:
        self._root = None


    def add(self, left_node, right_node, parent_node):
        """
        Add possible board state.
        """
        left_node = BTNode(left_node)
        left_node.parent = parent_node
        right_node = BTNode(right_node)
        right_node.parent = parent_node
        parent_node.left = left_node
        parent_node.right = right_node
