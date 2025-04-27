def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 times the "." character
    '''
    return [['.'] * 3 for _ in range(3)]


def display_board(board):
    print("      1   2   3")
    row_labels = ['A', 'B', 'C']
    for i, row in enumerate(board):
        print(f"  {row_labels[i]}   {' | '.join(row)} ")
        if i < 3:
            print("     ---+---+---")


def is_board_full(board):
    for row in board:
        if '.' in row:
            return False
    return True


def get_winning_player(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None


if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
        ['X', "O", "."],
        ['X', "O", "."],
        ['0', "X", "."]
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    display_board(board)
    
    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1))

    board_2 = [
        [".", "O", "O"],
        [".", "O", "X"],
        [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2))

    board_3 = [
        ["O", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3))

    board_4 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))
