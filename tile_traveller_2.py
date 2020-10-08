import random
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
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
def print_directions(directions_str):
    '''Prinst available directions to travel to'''
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
def play_one_move(col, row, valid_directions, random_picked):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    if random_picked:
        direction = random_directions()
        print('Direction:', direction)
    else:
        direction = direction.lower()
        direction = input("Direction:", direction)
    if not direction in valid_directions:
        print("Not a valid direction!")
        direction_valid = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        direction_valid = True
    return victory, col, row, direction_valid
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
def lever_on_tile(col,row):
    '''check if player is on a lever tile'''
    lever = False
    if col == 1 and row == 2:
        lever = True
    elif col == 2 and row == 2:
        lever = True
    elif col == 2 and row == 3:
        lever = True
    elif col == 3 and row == 2:
        lever = True
    return lever
def lever_can_be_pulled(direction_valid):
    '''Checks if direction was valid or invalid before'''
    if direction_valid: # Comes from Play_one_move function
        return True
    else:
        return False
def get_input_lever(random_picked):
    '''Gets input wether player wants to pull lever'''
    if random_picked:
        pull_lever = random_pull_lever()
        print('Pull a lever (y/n):', pull_lever)
    else:
        pull_lever = 'x'
        first = True
        while pull_lever not in 'yn':
            if not first:
                print('Invalid!')
            pull_lever = input('Pull a lever (y/n): ').lower()
            first = False
    return pull_lever
def random_directions():
    return random.choice([NORTH,EAST,SOUTH,WEST])
def random_pull_lever():
    return random.choice(['y','n'])
def pick_seed():
    seed = int(input('Input seed: '))
    return random.seed(seed)
def get_input_random():
    '''Gets input wether player wants to pull lever'''
    rand_choice = 'x'
    first = True
    while rand_choice not in 'rs':
        if not first:
            print('Invalid!')
        rand_choice = input('Play randomly or yourself (r/s): ').lower()
        first = False
    return rand_choice

# The main program starts here
def main():
    victory = False
    direction_valid = True
    coins = 0
    row = 1
    col = 1
    random_picked = True
    counter = 0
    pick_seed()
    while not victory:
        valid_directions = find_directions(col, row)
        # If player is on lever tile and direction was valid before
        if lever_on_tile(col, row) and lever_can_be_pulled(direction_valid):
            pull_lever = get_input_lever(random_picked)
            # If player decides to pull lever
            if pull_lever == 'y':
                coins += 1
                print('You received 1 coin, your total is now {}.'.format(coins))
        print_directions(valid_directions)
        victory, col, row, direction_valid = play_one_move(col, row, valid_directions, random_picked)
        counter += 1
    print("Victory! Total coins {}. Moves {}.".format(coins, counter))
play = 'y'
while play == 'y':
    #play_random = get_input_random():
    main()
    play = input('Play again (y/n): ')