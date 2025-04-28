def get_menu_option():
  while True:
    print("\nTic-Tac-Toe Game Menu:")
    print("1. Human vs Human")
    print("2. Random AI vs Random AI")
    print("3. Human vs Random AI")
    print("4. Human vs Unbeatable AI")
    
    try:
      choice = int(input("\nSelect game mode (1-4): "))
      if 1 <= choice <= 4:
        return choice
      else:
        print("Please enter a number between 1 and 4.")
    except ValueError:
      print("Please enter a valid number.")


if __name__ == "__main__":
    option = get_menu_option()
    print(option) 