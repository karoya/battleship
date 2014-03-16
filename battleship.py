from random import randint

board = []

print "Let's play Battleplane!"

no_players = int(raw_input("Number of players:"))

size = int(raw_input("Size of the battleground"))

no_turns = 4

for x in range(size):
    board.append(["O"] * size)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col


for turn in range(no_turns):
    for player in range(no_players):

        print "Player: ", player + 1
        print "Turn: ", turn + 1 

        print_board(board)
        
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if (guess_row < 0 or guess_row > size) or (guess_col < 0 or guess_col > size):
                print "Oops, that's not even in the ocean."
        else:
            if board[guess_row][guess_col] == "*":
                print "You guessed that one already."
            elif turn == 3:
                print "Game Over"
            elif guess_row == ship_row and guess_col == ship_col:
                print "Congratulations! You sunk my battleship!"
                board[guess_row][guess_col] = "X"
                break
            else: 
                print "You missed my battleplane!"
            board[guess_row][guess_col] = "*"

           
    if guess_row == ship_row and guess_col == ship_col:
        break
print_board(board) 
