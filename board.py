"""Board state"""

from btree import BTree
from btnode import BTNode
import copy

class Board:
    """Represent game board"""
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.symbol = None
        self.position = None


    def get_status(self, board=None):
        """
        Check status of game.
        """

        if not board:
            board = self.board
        patterns = [[(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 0), (1, 0), (2, 0)],
                    [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)],
                    [(0, 2), (1, 1), (2, 0)]]
        for i in patterns:
            if board[i[0][0]][i[0][1]] == board[i[1][0]][i[1][1]]\
               == self.board[i[2][0]][i[2][1]] == 'x':
                return 'x'
            elif board[i[0][0]][i[0][1]] == board[i[1][0]][i[1][1]]\
                 == board[i[2][0]][i[2][1]] == '0':
                return '0'
            else:
                continue
        for j in board:
            for k in j:
                if k == ' ':
                    return 'continue'
        return 'draw'


    def make_move(self, position, turn):
        """
        Make move.
        """
        if self.board[position[0]][position[1]] == ' ':
            self.board[position[0]][position[1]] = turn
            self.symbol = turn
            self.position = position
        else:
            raise IndexError


    def make_computer_move(self):
        """
        Computer makes move.
        """
        choice = self.computer_choice()
        position = choice.position
        turn = choice.data[position[0]][position[1]]
        self.make_move(position, turn)

    
    def build_tree(self):
        """
        Build a tree.
        """
        tree = BTree()
        tree._root = BTNode(self.board)
        def recurce(node, turn):
            if node and self.get_status(node.data) == 'continue':
                self._check_state(node)
                move_1, move_2, position_1, position_2 = self._find_moves(node, turn)
                turn = 'x' if turn == '0' else '0'
                tree.add(move_1, move_2, node)
                node.left.position = position_1
                node.right.position = position_2
                recurce(node.left, turn)
                recurce(node.right, turn)
        recurce(tree._root, '0')
        return tree
            

    def _check_state(self, node):
        """
        Return points.
        """
        status = self.get_status(node.data)
        if status == '0':
            node.points = 1
        elif status == 'x':
            node.points = -1


    def _find_moves(self, node, turn):
        """
        Find possible moves.
        """
        count = 0
        position_1 = None
        data_1 = copy.deepcopy(node.data)
        for i in range(3):
            for j in range(3):
                if data_1[i][j] == ' ' and count < 1:
                    data_1[i][j] = turn
                    position_1 = (i, j)
                    count += 1
        count = 0
        position_2 = None
        data_2 = copy.deepcopy(data_1)
        for m in range(3):
            for n in range(3):
                if data_2[m][n] == ' ' and count < 1:
                    data_2[m][n] = turn
                    position_2 = (m, n)
                    count += 1
        if data_2 == data_1:
            return data_1, data_1, position_1, position_1
        else:
            data_2[position_1[0]][position_1[1]] = ' '
            return data_1, data_2, position_1, position_2


    def computer_choice(self):
        """
        Choose move.
        """
        tree = self.build_tree()
        self._points_for_choice(tree._root.left)
        self._points_for_choice(tree._root.right)
        if tree._root.left.points >= tree._root.right.points:
            return tree._root.left
        else:
            return tree._root.right


    def _points_for_choice(self, node):
        """
        Count points.
        """
        count = 0
        def recurce(node, count):
            if node:
                count += node.points
                recurce(node.left, count)
                recurce(node.right, count)
        recurce(node, 0)
        return count
        

    def __str__(self) -> str:
        """
        String representation of board.
        """
        string = ''
        for i in self.board:
            string += str(i) + '\n'
        return string[:-1]
