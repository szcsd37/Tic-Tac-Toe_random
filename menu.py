def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
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
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    # print("If the user selected 1, it should print 1")
    print(option) 