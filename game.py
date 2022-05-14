"""Game flow"""
from board import Board


print('Welcome to cross-zero game')
print('It`s your turn')

board = Board()
while True:
    if board.get_status() == '0':
        print('You lose')
        break
    elif board.get_status() == 'x':
        print('You win')
        break
    print(board)
    print(board.get_status())
    position_1 = int(input('Enter row: '))
    position_2 = int(input('Enter column: '))
    try:
        board.make_move((position_1, position_2), 'x')
        print(board)
        if board.get_status() == '0':
            print('You lose')
            break
        elif board.get_status() == 'x':
            print('You win')
            break
        print(board.get_status())
        board.make_computer_move()
    except IndexError:
        print('This is not valid position')
