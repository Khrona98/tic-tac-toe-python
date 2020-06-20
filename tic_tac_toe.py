# Tic Tac Toe in Python


def player_marker(player1, player2):
    """Take both players input for the markers."""
    # check if player1 is 'X' or 'O'
    while player1 != "X" and player1 != "O":
        try:
            player1 = input("Please pick a marker ('X' or 'O'): ").upper()

        except ValueError:
            print("This is not a valid marker, please try again!")
            print()

    print()

    if player1 == "X":
        player2 = "O"
        print(
            f"Player 1 is '{player1}'."
            f"\nPlayer 2 is '{player2}'."
            "\n\nNow you will have to choose from 1 - 9 where '1' is the "
            "left lower corner and '9' is the right upper corner."
        )
        input("Press Enter to continue. ")

    elif player1 == "O":
        player2 = "X"
        print(
            f"Player 1 is '{player1}'."
            f"\nPlayer 2 is '{player2}'."
            "\n\nNow you will have to choose from 1 - 9 where '1' is the "
            "left lower corner and '9' is the right upper corner."
        )
        input("Press Enter to continue. ")

    # return both variables to reassign then locally on the game_logic() function
    return (player1, player2)


def p1_marker_loc(p1_input, board_list, player1):
    """Take the location of the marker for Player 1."""
    # verify if the input is not in range or in range but in a already taken spot
    while p1_input not in range(1, 10) or (
        p1_input in range(1, 10) and board_list[p1_input] != " "
    ):
        try:
            p1_input = int(
                input("Player 1: Where would you like to place the marker (1 - 9)? ")
            )

            # if a marker is already placed on that board location, display a message
            # warning player 1 and ask for their input again
            if board_list[p1_input] != " ":
                print(
                    "There is already a marker there, please choose another location."
                )
                input("Press Enter to continue. ")
                print()

                # input the player for another location for the marker
                continue

        except ValueError:
            print("This is not a number, please try again!")
            print()

    print(f"Player 1 is placing {player1} in position {p1_input}.")

    # return the variable to reassign it locally on the game_logic() function
    return p1_input


def p2_marker_loc(p2_input, board_list, player2):
    """Take the location of the marker for Player 2."""
    # verify if the input is not in range or in range but in a already taken spot
    while p2_input not in range(1, 10) or (
        p2_input in range(1, 10) and board_list[p2_input] != " "
    ):
        try:
            p2_input = int(
                input("Player 2: Where would you like to place the marker (1 - 9)? ")
            )

            # if a marker is already placed on that board location, display a message
            # warning player 2 and ask for their input again
            if board_list[p2_input] != " ":
                print(
                    "There is already a marker there, please choose another location."
                )
                input("Press Enter to continue. ")
                print()

                # input the player for another location for the marker
                continue

        except ValueError:
            print("This is not a number, please try again!")
            print()

    print(f"Player 2 is placing {player2} in position {p2_input}.")

    # return the variable to reassign it locally on the game_logic() function
    return p2_input


def board(board_list):
    """Draw the board on the screen with the welcoming message."""
    print(
        f"   {board_list[7]}  |  {board_list[8]}  |  {board_list[9]}   "
        f"\n {'-' * 17} \n"
        f"   {board_list[4]}  |  {board_list[5]}  |  {board_list[6]}   "
        f"\n {'-' * 17} \n"
        f"   {board_list[1]}  |  {board_list[2]}  |  {board_list[3]}   "
    )


def x_win_condition(board_list):
    """Condition for 'X' to win."""
    return (
        (board_list[1] == "X" and board_list[2] == "X" and board_list[3] == "X")
        or (board_list[1] == "X" and board_list[4] == "X" and board_list[7] == "X")
        or (board_list[1] == "X" and board_list[5] == "X" and board_list[9] == "X")
        or (board_list[2] == "X" and board_list[5] == "X" and board_list[8] == "X")
        or (board_list[3] == "X" and board_list[6] == "X" and board_list[9] == "X")
        or (board_list[3] == "X" and board_list[5] == "X" and board_list[7] == "X")
        or (board_list[4] == "X" and board_list[5] == "X" and board_list[6] == "X")
        or (board_list[7] == "X" and board_list[8] == "X" and board_list[9] == "X")
    )


def o_win_condition(board_list):
    """Condition for 'O' to win."""
    return (
        (board_list[1] == "O" and board_list[2] == "O" and board_list[3] == "O")
        or (board_list[1] == "O" and board_list[4] == "O" and board_list[7] == "O")
        or (board_list[1] == "O" and board_list[5] == "O" and board_list[9] == "O")
        or (board_list[2] == "O" and board_list[5] == "O" and board_list[8] == "O")
        or (board_list[3] == "O" and board_list[6] == "O" and board_list[9] == "O")
        or (board_list[3] == "O" and board_list[5] == "O" and board_list[7] == "O")
        or (board_list[4] == "O" and board_list[5] == "O" and board_list[6] == "O")
        or (board_list[7] == "O" and board_list[8] == "O" and board_list[9] == "O")
    )


def tie_condition(board_list):
    """Condition for a tie to happen."""
    return " " not in board_list[1:10]


def p1_won():
    """Declare Player 1 as the winner."""
    print("PLAYER 1 WON!")
    print("CONGRATULATIONS!")


def p2_won():
    """Declare Player 2 as the winner."""
    print("PLAYER 2 WON!")
    print("CONGRATULATIONS!")


def tie_message():
    """Declare the game as a tie."""
    print("IT'S A TIE!")


def game_logic():
    """Dictates how the game works."""
    # variables for the player_marker() function
    player1 = None
    player2 = None

    # variables for the p1_marker_loc() and p2_marker_loc() functions
    p1_input = None
    p2_input = None

    # variable for the board() function
    board_list = [" "] * 10

    # cleaning the terminal and displaying the welcoming message
    print("\n" * 100)
    print("WELCOME TO TIC TAC TOE IN PYTHON")
    print()
    board(board_list)
    print()

    # get the marker for each player
    player1, player2 = player_marker(player1, player2)
    print()

    # keep looping the core gameplay until either the win or tie conditions are met
    while True:

        # check if someone won
        if x_win_condition(board_list):

            # declare who is the winner and break from the loop
            if player1 == "X":
                p1_won()
                print()
                break

            elif player2 == "X":
                p2_won()
                print()
                break

        # check if someone won
        elif o_win_condition(board_list):

            # declare who is the winner and break from the loop
            if player1 == "O":
                p1_won()
                print()
                break

            elif player2 == "O":
                p2_won()
                print()
                break

        # check if it is a tie
        elif tie_condition(board_list):
            tie_message()
            print()
            break

        else:
            # get the location of the marker for player 1
            p1_input = p1_marker_loc(p1_input, board_list, player1)

            # assign player1 to specific indexes at the board list
            board_list[p1_input] = player1
            print()

            # display the marker on the board
            print("\n" * 100)
            print("TIC TAC TOE IN PYTHON")
            print()
            board(board_list)
            print()

        # check if someone won
        if x_win_condition(board_list):

            # declare who is the winner and break from the loop
            if player1 == "X":
                p1_won()
                print()
                break

            elif player2 == "X":
                p2_won()
                print()
                break

        # check if someone won
        elif o_win_condition(board_list):

            # declare who is the winner and break from the loop
            if player1 == "O":
                p1_won()
                print()
                break

            elif player2 == "O":
                p2_won()
                print()
                break

        # check if it is a tie
        elif tie_condition(board_list):
            tie_message()
            print()
            break

        else:
            # get the location of the marker for player 2
            p2_input = p2_marker_loc(p2_input, board_list, player2)

            # assign player2 to specific indexes at the board list
            board_list[p2_input] = player2
            print()

            # display the marker on the board
            print("\n" * 100)
            print("TIC TAC TOE IN PYTHON")
            print()
            board(board_list)
            print()


game_logic()


def game_restart():
    """Ask the players if they want to continue playing."""
    # continue looping the question if the player's answer is not 'Y/YES' or 'N/NO'
    while True:
        reboot = input("Would you like to play again? (Y/N) ").upper()
        print()

        if reboot == "Y" or reboot == "YES":
            game_logic()

        elif reboot == "N" or reboot == "NO":
            print("Thanks for playing!")
            print()
            break


game_restart()
