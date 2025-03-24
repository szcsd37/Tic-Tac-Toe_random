import random

def get_human_coordinates(board, current_player):
    while True:
        user_input = input("Enter coordinates (A-C,1-3) or 'quit' to exit: ").strip().upper()
        
        if user_input == "QUIT":
            exit()
        
        if len(user_input) == 2 and user_input[0] in "ABC" and user_input[1] in "123":
            row = "ABC".index(user_input[0])
            col = int(user_input[1]) - 1
            
            if board[row][col] == ".":
                return row, col
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Use format: Letter (A-C) and Number (1-3), e.g., A1.")

def get_random_ai_coordinates(board, current_player):
    available_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == "."]
    return random.choice(available_spots) if available_spots else None

def get_unbeatable_ai_coordinates(board, current_player):
    def check_winner(board, player):
        for row in board:
            if row.count(player) == 3:
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    opponent = "X" if current_player == "O" else "O"
    available_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == "."]
    
    for r, c in available_spots:
        board[r][c] = current_player
        if check_winner(board, current_player):
            return r, c
        board[r][c] = "."
    
    for r, c in available_spots:
        board[r][c] = opponent
        if check_winner(board, opponent):
            return r, c
        board[r][c] = "."
    
    return available_spots[0] if available_spots else None

if __name__ == "__main__":
    board_1 = [["X", "X", "."], ["X", ".", "."], ["X", "X", "."]]
    print("It should print the coordinates selected by the human player")
    # Uncomment the line below to test user input
    # coordinates = get_human_coordinates(board_1, "X")
    # print(coordinates)

    board_2 = [["O", "O", "."], ["X", "O", "."], ["X", "X", "O"]]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "X"))

    board_3 = [["O", "X", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3, "X"))

    board_4 = [[".", "O", "."], ["X", "O", "."], ["X", "X", "O"]]
    print("The printed coordinate should always be (0, 0)")
    print(get_unbeatable_ai_coordinates(board_4, "X")) 

    board_5 = [["X", "O", "."], ["X", ".", "."], ["O", "O", "X"]]
    print("The printed coordinate should always be (1, 1)")
    print(get_unbeatable_ai_coordinates(board_5, "O")) 

    board_6 = [["O", "O", "."], ["O", "X", "."], [".", "X", "."]]
    print("The printed coordinate should either (0, 2) or (2, 0)")
    print(get_unbeatable_ai_coordinates(board_6, "X"))
