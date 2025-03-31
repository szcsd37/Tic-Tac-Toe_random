import random
import math

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
    opponent = "X" if current_player == "O" else "O"
    
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
    
    def minimax(board, depth, is_maximizing):
        if check_winner(board, current_player):
            return 10 - depth
        if check_winner(board, opponent):
            return depth - 10
        if all(board[r][c] != "." for r in range(3) for c in range(3)):
            return 0

        if is_maximizing:
            best_score = -math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ".":
                        board[r][c] = current_player
                        score = minimax(board, depth + 1, False)
                        board[r][c] = "."
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ".":
                        board[r][c] = opponent
                        score = minimax(board, depth + 1, True)
                        board[r][c] = "."
                        best_score = min(best_score, score)
            return best_score
    
    best_move = None
    best_score = -math.inf
    for r in range(3):
        for c in range(3):
            if board[r][c] == ".":
                board[r][c] = current_player
                score = minimax(board, 0, False)
                board[r][c] = "."
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    
    return best_move

if __name__ == "__main__":
    board_1 = [["X", "X", "."], ["X", ".", "."], ["X", "X", "."]]
    print("It should print the coordinates selected by the human player")

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
