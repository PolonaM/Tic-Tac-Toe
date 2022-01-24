"""
This is a Tic Tac Toe game for 2 human players.
It is played on the same keyboard on the numpad.
Numbers on the numpad match the grid of the tic tac toe board which looks like this:
_7_|_8_|_9_
_4_|_5_|_6_
 1 | 2 | 3
Trough the user input the user then provides a number where to place the x/o.
"""

from random import randint
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]}  ')
    print('-----------------')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]}  ')
    print('-----------------')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]}  ')


def clear_board():
    return [' ',' ',' ',' ',' ',' ',' ',' ',' ']


def player_input():
    possible_input = ['X','O','x','o']
    player1_select = True

    while player1_select:
        player1_marker = input('Player 1, select X or O: ')
        if player1_marker in possible_input:
            if player1_marker == 'X':
                player2_marker = 'O'
            else:
                player2_marker = 'X'
            player1_select = False
        else:
            print('Wrong input!')

    return player1_marker, player2_marker


def place_marker(board, marker, position):
    board[position-1] = marker

    return board


def win_check(board, mark, player):
    # The preferred way of wrapping long lines is by using Python's implied line continuation
    # inside parentheses, brackets and braces.
    # If necessary, you can add an extra pair of parentheses around an expression,
    # but sometimes using a backslash looks better.
    # Make sure to indent the continued line appropriately.
    # The preferred place to break around a binary operator is after the operator, not before it.
    if (board[0] == board[1] == board[2] == mark or board[3] == board[4] == board[5] == mark or
        board[6] == board[7] == board[8] == mark or board[0] == board[3] == board[6] == mark or
        board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or
        board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark):
        print(f'Game over! {player} won!')
        return True
    else:
        return False


def choose_first():
    if randint(1,2) == 1:
        print('Player 1 starts first!')
        return 'Player 1'
    else:
        print('Player 2 starts first!')
        return 'Player 2'


def space_check(board, position):
    if board[position-1] == ' ':
        return True
    else:
        print("Sorry, but the field is already full!")
        return False


def full_board_check(board):
    if ' ' in board:
        return False
    else:
        print('The board is full!')
        return True


def player_choice(board, player):
    choice = 'wrong'

    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input(f"{player}, choose the field (1-9): ")
        if choice in ['1','2','3','4','5','6','7','8','9']:
            if space_check(board, int(choice)):
                continue
            else:
                choice = 'wrong'
        else:
            print("Sorry, but you did not choose a value in the correct range (1-9)!")

    return int(choice)



def replay():
    choice = 'wrong'

    while choice not in ['Y','N','y','n']:
        choice = input("Would you like to keep playing? (Y or N): ")
        if choice not in ['Y','N']:
            clear_output()
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    clear_output()

    return bool(choice == "Y")


gameon = True
[player1_marker, player2_marker] = player_input()

while gameon:
    board = clear_board()
    display_board(board)
    result = choose_first()

    if result == 'Player 1':
        marker1 = player1_marker
        marker2 = player2_marker
        player1 = 'Player 1'
        player2 = 'Player 2'
    else:
        marker1 = player2_marker
        marker2 = player1_marker
        player1 = 'Player 2'
        player2 = 'Player 1'

    gameon = True

    while gameon:

        #PLAYER 1
        position = player_choice(board, player1)

        board = place_marker(board, marker1, position)
        display_board(board)

        if win_check(board, marker1, player1):
            break
        if full_board_check(board):
            break

        #PLAYER 2
        position = player_choice(board, player2)

        board = place_marker(board, marker2, position)
        display_board(board)

        if win_check(board, marker2, player2):
            break
        if full_board_check(board):
            break

    gameon = replay()
