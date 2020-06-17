# Tic Tac Toe in Python

# global variables for the player_marker() function, assigned to None as filler
player1 = None
player2 = None

# global variables for the p1_marker_loc() and p2_marker_loc() functions
p1_input = None
p2_input = None

# global variables for the board() function
marker1 = " "
marker2 = " "
marker3 = " "
marker4 = " "
marker5 = " "
marker6 = " "
marker7 = " "
marker8 = " "
marker9 = " "


def player_marker():
    """Take both players input for the markers."""
    global player1
    global player2

    # check if player1 is 'X' or 'O'
    while player1 != "X" and player1 != "O":
        player1 = input("Please pick a marker ('X' or 'O'): ").upper()

    print()

    if player1 == "X":
        player2 = "O"
        print(
            "Player 1 is 'X'."
            "\nPlayer 2 is 'O'."
            "\n\nNow you will have to choose from 1 - 9 where '1' is the "
            "left lower corner and '9' is the right upper corner."
        )
        input("Press Enter to continue. ")

    elif player1 == "O":
        player2 = "X"
        print(
            "Player 1 is 'O'."
            "\nPlayer 2 is 'X'."
            "\n\nNow you will have to choose from 1 - 9 where '1' is the "
            "left lower corner and '9' is the right upper corner."
        )
        input("Press Enter to continue. ")


def p1_marker_loc():
    """Take the location of the marker for Player 1."""
    global p1_input

    # verify if the input is not in range
    while p1_input not in range(1, 10):
        try:
            p1_input = int(
                input("Player 1: Where would you like to place the marker (1 - 9)? ")
            )

            # if the marker is already placed on the board, display a message warning
            # the players and ask for their input again
            while (
                (p1_input == 1 and marker1 != " ")
                or (p1_input == 2 and marker2 != " ")
                or (p1_input == 3 and marker3 != " ")
                or (p1_input == 4 and marker4 != " ")
                or (p1_input == 5 and marker5 != " ")
                or (p1_input == 6 and marker6 != " ")
                or (p1_input == 7 and marker7 != " ")
                or (p1_input == 8 and marker8 != " ")
                or (p1_input == 9 and marker9 != " ")
            ):
                print(
                    "There is already a marker there, please choose another location."
                )
                input("Press Enter to continue. ")
                print()

                try:
                    p1_input = int(
                        input(
                            "Player 1: Where would you like to place "
                            "the marker (1 - 9)? "
                        )
                    )

                except ValueError:
                    print("This is not a number, please try again!")

        except ValueError:
            print("This is not a number, please try again!")

    print(f"Player 1 is placing {player1} in position {p1_input}.")


def p2_marker_loc():
    """Take the location of the marker for Player 2."""
    global p2_input

    # verify if the input is not in range
    while p2_input not in range(1, 10):
        try:
            p2_input = int(
                input("Player 2: Where would you like to place the marker (1 - 9)? ")
            )

            # if the marker is already placed on the board, display a message warning
            # the players and ask for their input again
            while (
                (p2_input == 1 and marker1 != " ")
                or (p2_input == 2 and marker2 != " ")
                or (p2_input == 3 and marker3 != " ")
                or (p2_input == 4 and marker4 != " ")
                or (p2_input == 5 and marker5 != " ")
                or (p2_input == 6 and marker6 != " ")
                or (p2_input == 7 and marker7 != " ")
                or (p2_input == 8 and marker8 != " ")
                or (p2_input == 9 and marker9 != " ")
            ):
                print(
                    "There is already a marker there, please choose another location."
                )
                input("Press Enter to continue. ")
                print()

                try:
                    p2_input = int(
                        input(
                            "Player 2: Where would you like to place "
                            "the marker (1 - 9)? "
                        )
                    )

                except ValueError:
                    print("This is not a number, please try again!")

        except ValueError:
            print("This is not a number, please try again!")

    print(f"Player 2 is placing {player2} in position {p2_input}.")


# fmt: off
# function to draw the board on the screen
def board():
    """Draw the board on the screen."""
    board_dict = {
        1: f" {marker1} |", 2: f" {marker2} ", 3: f"| {marker3} ",
        4: f" {marker4} |", 5: f" {marker5} ", 6: f"| {marker6} ",
        7: f" {marker7} |", 8: f" {marker8} ", 9: f"| {marker9} ",
    }

    print(
        f"  {board_dict[7]} {board_dict[8]} {board_dict[9]} \n {'-' * 15} \n"
        f"  {board_dict[4]} {board_dict[5]} {board_dict[6]} \n {'-' * 15} \n"
        f"  {board_dict[1]} {board_dict[2]} {board_dict[3]}"
    )
# fmt: on


# assigning the player move to each correspondent marker
def board_markdown():
    """Assign the player move to each correspondent marker."""
    global marker1

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker1 == " ":
        if p1_input == 1:
            marker1 = player1

        elif p2_input == 1:
            marker1 = player2

    global marker2

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker2 == " ":
        if p1_input == 2:
            marker2 = player1

        elif p2_input == 2:
            marker2 = player2

    global marker3

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker3 == " ":
        if p1_input == 3:
            marker3 = player1

        elif p2_input == 3:
            marker3 = player2

    global marker4

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker4 == " ":
        if p1_input == 4:
            marker4 = player1

        elif p2_input == 4:
            marker4 = player2

    global marker5

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker5 == " ":
        if p1_input == 5:
            marker5 = player1

        elif p2_input == 5:
            marker5 = player2

    global marker6

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker6 == " ":
        if p1_input == 6:
            marker6 = player1

        elif p2_input == 6:
            marker6 = player2

    global marker7

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker7 == " ":
        if p1_input == 7:
            marker7 = player1

        elif p2_input == 7:
            marker7 = player2

    global marker8

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker8 == " ":
        if p1_input == 8:
            marker8 = player1

        elif p2_input == 8:
            marker8 = player2

    global marker9

    # if the marker isn't already assigned to either 'X' or 'O'
    # assign it to the correspondent player
    if marker9 == " ":
        if p1_input == 9:
            marker9 = player1

        elif p2_input == 9:
            marker9 = player2


def game_logic():
    """Dictates how the game works."""
    # cleaning the terminal and displaying the welcoming message
    print("\n" * 100)
    print("WELCOME TO TIC TAC TOE IN PYTHON")
    print()
    board()
    print()

    # get the marker for each player
    player_marker()
    print()

    # keep looping the core gameplay until either the win condition
    # or the tie condition is met
    while True:

        # check if the first player won and brake the loop
        if (
            (marker1 == "X" and marker2 == "X" and marker3 == "X")
            or (marker1 == "X" and marker4 == "X" and marker7 == "X")
            or (marker1 == "X" and marker5 == "X" and marker9 == "X")
            or (marker2 == "X" and marker5 == "X" and marker8 == "X")
            or (marker3 == "X" and marker6 == "X" and marker9 == "X")
            or (marker3 == "X" and marker5 == "X" and marker7 == "X")
            or (marker4 == "X" and marker5 == "X" and marker6 == "X")
            or (marker7 == "X" and marker8 == "X" and marker9 == "X")
        ):

            # declare who is the winner and break from the loop
            if player1 == "X":
                print("PLAYER 1 WON!")
                print("CONGRATULATIONS!")
                print()

                break

            elif player2 == "X":
                print("PLAYER 2 WON!")
                print("CONGRATULATIONS!")
                print()

                break

        # check if the second player won and brake the loop
        elif (
            (marker1 == "O" and marker2 == "O" and marker3 == "O")
            or (marker1 == "O" and marker4 == "O" and marker7 == "O")
            or (marker1 == "O" and marker5 == "O" and marker9 == "O")
            or (marker2 == "O" and marker5 == "O" and marker8 == "O")
            or (marker3 == "O" and marker6 == "O" and marker9 == "O")
            or (marker3 == "O" and marker5 == "O" and marker7 == "O")
            or (marker4 == "O" and marker5 == "O" and marker6 == "O")
            or (marker7 == "O" and marker8 == "O" and marker9 == "O")
        ):

            # declare who is the winner and break from the loop
            if player1 == "O":
                print("PLAYER 1 WON!")
                print("CONGRATULATIONS!")
                print()

                break

            elif player2 == "O":
                print("PLAYER 2 WON!")
                print("CONGRATULATIONS!")
                print()

                break

        # check if it is a tie
        elif " " not in (
            marker1,
            marker2,
            marker3,
            marker4,
            marker5,
            marker6,
            marker7,
            marker8,
            marker9,
        ):
            print("IT'S A TIE!")
            print()

            break

        else:
            # get the location of the marker for player 1
            p1_marker_loc()
            print()

            # display the marker on the board
            board_markdown()
            print("\n" * 100)
            print("TIC TAC TOE IN PYTHON")
            print()
            board()
            print()

        # check if the first player won and brake the loop
        if (
            (marker1 == "X" and marker2 == "X" and marker3 == "X")
            or (marker1 == "X" and marker4 == "X" and marker7 == "X")
            or (marker1 == "X" and marker5 == "X" and marker9 == "X")
            or (marker2 == "X" and marker5 == "X" and marker8 == "X")
            or (marker3 == "X" and marker6 == "X" and marker9 == "X")
            or (marker3 == "X" and marker5 == "X" and marker7 == "X")
            or (marker4 == "X" and marker5 == "X" and marker6 == "X")
            or (marker7 == "X" and marker8 == "X" and marker9 == "X")
        ):

            # declare who is the winner and break from the loop
            if player1 == "X":
                print("PLAYER 1 WON!")
                print("CONGRATULATIONS!")
                print()

                break

            elif player2 == "X":
                print("PLAYER 2 WON!")
                print("CONGRATULATIONS!")
                print()

                break

        # check if the second player won and brake the loop
        elif (
            (marker1 == "O" and marker2 == "O" and marker3 == "O")
            or (marker1 == "O" and marker4 == "O" and marker7 == "O")
            or (marker1 == "O" and marker5 == "O" and marker9 == "O")
            or (marker2 == "O" and marker5 == "O" and marker8 == "O")
            or (marker3 == "O" and marker6 == "O" and marker9 == "O")
            or (marker3 == "O" and marker5 == "O" and marker7 == "O")
            or (marker4 == "O" and marker5 == "O" and marker6 == "O")
            or (marker7 == "O" and marker8 == "O" and marker9 == "O")
        ):

            # declare who is the winner and break from the loop
            if player1 == "O":
                print("PLAYER 1 WON!")
                print("CONGRATULATIONS!")
                print()

                break

            elif player2 == "O":
                print("PLAYER 2 WON!")
                print("CONGRATULATIONS!")
                print()

                break

        # check if it is a tie
        elif " " not in (
            marker1,
            marker2,
            marker3,
            marker4,
            marker5,
            marker6,
            marker7,
            marker8,
            marker9,
        ):
            print("IT'S A TIE!")
            print()

            break

        else:
            # get the location of the marker for player 2
            p2_marker_loc()
            print()

            # verify if the markers are different then display it on the board
            board_markdown()
            print("\n" * 100)
            print("TIC TAC TOE IN PYTHON")
            print()
            board()
            print()

            # reset the global input variables so the markers can be reassigned properly
            global p1_input
            p1_input = None

            global p2_input
            p2_input = None


game_logic()

while True:
    game_reboot = input("Would you like to play again? (Y/N) ").upper()
    print()

    if game_reboot == "Y" or game_reboot == "YES":
        # reset the global variables to be able to restart the game properly
        # global variables for the player_marker() function, assigned to None as filler
        player1 = None
        player2 = None

        # global variables for the p1_marker_loc() and p2_marker_loc() functions
        p1_input = None
        p2_input = None

        # global variables for the board() function
        marker1 = " "
        marker2 = " "
        marker3 = " "
        marker4 = " "
        marker5 = " "
        marker6 = " "
        marker7 = " "
        marker8 = " "
        marker9 = " "

        # restart the game after the global variables above have been reset to default
        game_logic()

    elif game_reboot == "N" or game_reboot == "NO":
        print("Thanks for playing!")
        print()
        break
