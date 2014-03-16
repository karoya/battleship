from random import randint

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row1(board):
    return randint(0, len(board) - 1)

def random_col1(board):
    return randint(0, len(b) - 1)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def relationship(size):
    no_ships = 0
    for i in range(size / 4):
        no_ships += 1
    return no_ships

def location_of_ships(no_ships, board):
    ships = []
    for ship in range(no_ships):
        ship_row = random_row(board)
        ship_col = random_col(board)
        one_ship = [ship_row, ship_col]
        ships.append(one_ship)
    print ships
    return ships

def check(guess_row, guess_col, ships):
    if [guess_row, guess_col] in ships:
        return True
    else:
        return False
    
print "Let's play Battleplane!"

no_players = int(raw_input("Number of players:"))

size = int(raw_input("Size of the battleground"))

no_turns = 4

stunked_ships = 0

board = []

for x in range(size):
    board.append(["O"] * size)

ships = location_of_ships(relationship(size), board)

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
            if board[guess_row][guess_col] in ["*", "X"]:
                print "You guessed that one already."
            elif turn == 3:
                print "Game Over"
            elif check(guess_row, guess_col, ships):
                print "Congratulations! You sunk my battleship!"
                board[guess_row][guess_col] = "X"
                stunked_ships += 1
                if stunked_ships == len(ships): break
            else:
                board[guess_row][guess_col] = "*"
                print "You missed my battleplane!"
           

           
    if check(guess_row, guess_col, ships):
        if stunked_ships == len(ships): break
        
print_board(board) 
