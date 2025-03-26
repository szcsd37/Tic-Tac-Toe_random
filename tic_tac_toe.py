from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = 'X'  # Start with 'X'
    
    while is_game_running:
        display_board(board)
        
        # Determine move function based on game mode and current player
        if game_mode == HUMAN_VS_HUMAN:
            x, y = get_human_coordinates(board, current_player)
        elif game_mode == RANDOM_AI_VS_RANDOM_AI:
            x, y = get_random_ai_coordinates(board, current_player)
        elif game_mode == HUMAN_VS_RANDOM_AI:
            if current_player == 'X':
                x, y = get_human_coordinates(board, current_player)
            else:
                x, y = get_random_ai_coordinates(board)
        elif game_mode == HUMAN_VS_UNBEATABLE_AI:
            if current_player == 'X':
                x, y = get_human_coordinates(board, current_player)
            else:
                x, y = get_unbeatable_ai_coordinates(board, current_player)
        
        board[x][y] = current_player
        
        # Check for a winner or a tie
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)
        
        if winning_player:
            display_board(board)
            print(f"Player {winning_player} wins!")
            is_game_running = False
        elif its_a_tie:
            display_board(board)
            print("It's a tie!")
            is_game_running = False
        else:
            # Alternate the current player
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
