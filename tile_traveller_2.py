import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n' 
COIN_LIST = [(1,2),(2,2),(2,3),(3,2)]

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def coin_locator(row,col,coin_counter,seed):

    if (col,row) in coin_list:

        pull_lever = auto_lever(seed)

        if pull_lever == "y":

            coin_counter = coin_counter + 1
            print("You received 1 coin, your total is now {}.".format(coin_counter))

    return coin_counter

def pop_coin(col,row):

    if (col,row) in coin_list:

        coin_list.remove((col,row))

def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions,seed,move_counter):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    lever_bool = True
    direction = auto_mover(col,row,seed)
    move_counter +=1
    if not direction in valid_directions:
        print("Not a valid direction!")
        if (col,row) in coin_list:
            lever_bool = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        
    return victory, col, row, move_counter,lever_bool

def play_again():
    play = input("Play again (y/n): ")
    if play == "y":
        return True
    else:
        return False

def auto_mover(col,row,seed):
    dir_choice = random.choice([NORTH, EAST, SOUTH, WEST])
    print("Direction:",dir_choice)
    return dir_choice

def auto_lever(seed):
    lever_choice = random.choice([YES, NO])
    print("Pull a lever (y/n): {}".format(lever_choice))
    return lever_choice

# The main program starts here
play = True

while play:
    victory = False
    levers_bool = True
    seed_value = int(input('Input seed: '))
    random.seed(seed_value)
    moves = 0
    row = 1
    col = 1
    coins = 0  
    coin_list = [(1,2),(2,2),(2,3),(3,2)]
    while not victory:
        if levers_bool:    
            coins = coin_locator(row,col,coins,seed_value)
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, moves,levers_bool = play_one_move(col, row,\
             valid_directions,seed_value,moves)
    print("Victory! Total coins {}. Moves {}.".format(coins,moves))
    play = play_again()