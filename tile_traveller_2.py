import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n' 


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

def play_one_move(col, row, valid_directions,seed):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = auto_mover(col,row,seed)

    if not direction in valid_directions:
        print("Not a valid direction!")
        if (col,row) in coin_list:
            pop_coin(col,row)
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

def play_again():
    play = input("Play again (y/n): ")
    if play == "y":
        return True
    else:
        return False

def auto_mover(col,row,seed):
    random.seed(seed)

    dir_choice = random.choice([NORTH, EAST, SOUTH, WEST])
    return dir_choice

def auto_lever(seed):
    random.seed(seed)
       lever_choice = random.choice([YES, NO])

# The main program starts here
play = True
while play:
    victory = False
    row = 1
    col = 1
    coin_list = [(1,2),(2,2),(2,3),(3,2)]
    coins = 0  
    seed_value = input('Input seed: ')
    while not victory:
        coins = coin_locator(row,col,coins,seed_value)
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row = play_one_move(col, row, valid_directions,seed_value)
    print("Victory! Total coins {}.".format(coins))
    play = play_again()