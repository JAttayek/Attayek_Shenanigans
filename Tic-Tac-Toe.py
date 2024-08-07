# Tic-Tac-Toe Game Creation

# 1. Create the game board and pick list
# 2. Show the boards and ask for player1 input to start the game
# 3. Edit game board with user input, show new board, ask for player2 input
# 4. Check board after each play for winner. Continue gameplay until winner is achieved.
# 5. Show final game board, end loop, ask to play again?


#This will be the blank/iterable game board for the functions
game_board = "_|_|_\n_|_|_\n_|_|_"

#This is a visual for the user to choose a value from when picking a spot
option_board = "1|2|3\n4|5|6\n7|8|9"


#Provide the setup and current board
def game_setup():
    print("TIC_TAC_TOE\nAttayek Edition\n")
    print('Please choose a value from the reference board below:\n')
    print(option_board + "\n")
    print('Current game board:\n')
    print(game_board)


#Ask for player1 input
def player1():
    p1_move = 0
    while p1_move not in range(1,10):
        p1_move = int(input("Player 1 - Choose a value to place an X on the board: "))
    return p1_move


#Ask for player2 input
def player2():
    p2_move = 0
    while p2_move not in range(1,10):
        p2_move = int(input("Player 2 - Choose a value to place an O on the board: "))
    return p2_move


#Edit game board with player1 input
def edit_board_p1(game_board,choice):
    game_board = list(game_board)
    game_board[2*choice-2] = 'X'
    return "".join(game_board)

#Edit game board with player2 input
def edit_board_p2(game_board,choice):
    game_board = list(game_board)
    game_board[2*choice-2] = 'O'
    return "".join(game_board)


#Check to see if a winner exists
def check_winner(game_board):
    check_board = game_board.replace("\n","|").split("|")

    #Check horizontal rows
    if check_board[0:3] == ["X","X","X"] or check_board[0:3] == ["O","O","O"]:
        return True
    elif check_board[3:6] == ["X","X","X"] or check_board[3:6] == ["O","O","O"]:
        return True
    elif check_board[6:9] == ["X","X","X"] or check_board[6:9] == ["O","O","O"]:
        return True
    
    #Check vertical columns
    if check_board[0] == check_board[3]  == check_board[6] == "X" or check_board[0] == check_board[3]  == check_board[6] == "O":
        return True
    elif check_board[1] == check_board[4]  == check_board[7] == "X" or check_board[1] == check_board[4]  == check_board[7] == "O":
        return True
    elif check_board[2] == check_board[5]  == check_board[8] == "X" or check_board[2] == check_board[5]  == check_board[8] == "O":
        return True

    #Check diagonals
    if check_board[0] == check_board[4]  == check_board[8] == "X" or check_board[0] == check_board[4]  == check_board[8] == "O":
        return True
    elif check_board[2] == check_board[4]  == check_board[6] == "X" or check_board[2] == check_board[4]  == check_board[6] == "O":
        return True

    return False


#Check for a draw
def check_draw(game_board):
    if "_" not in game_board.replace("\n","|").split("|"):
        return True
    else:
        pass


from IPython.display import clear_output

#Iterable to continue game
in_progress = True

#This will be the blank/iterable game board for the functions
game_board = "_|_|_\n_|_|_\n_|_|_"

#This is a visual for the user to choose a value from when picking a spot
option_board = "1|2|3\n4|5|6\n7|8|9"

#Loop the game until a winner is found
while in_progress:

    #Show initial game board and options
    clear_output()
    game_setup()

    #Ask for player1 move
    choice = player1()
    #Input player1 move
    game_board = edit_board_p1(game_board,choice)
    #Check winner
    in_progress = not check_winner(game_board)

    #Show new board
    clear_output()
    game_setup()

    #Check for a draw
    if check_draw(game_board):
        print("\nDRAW!!! Try again.")
        break
    if not in_progress:
        print("\nCONGRATS PLAYER 1 IS THE WINNER!!!")
        continue

    #Ask for player2 move
    choice = player2()
    #Input player2 move
    game_board = edit_board_p2(game_board,choice)
    #Check winner
    in_progress = not check_winner(game_board)

    #Show new board
    clear_output()
    game_setup()

    if not in_progress:
        print("\nCONGRATS PLAYER 2 IS THE WINNER!!!")
        continue

#Pause command prompt screen from closing automatically
import os
os.system("pause")