
# Skilgreina function fyrir hverja átt
def north(x,y):
    y += 1
    return y
def south(x,y):
    y -= 1
    return y
def east(x,y):
    x += 1
    return x
def west(x,y):
    x -= 1
    return x
def boundaries(x,y,direction):
    #Kanna bannfærslur í hniti x,y
    #1,1-2,1 ; 2,1 - 3,1 ; 2,2-3,2 ; 2,2 -2,3 ; færslur bannaðar utan 1<= x,y <=3
    if x == 1 and y == 1 and (direction == "e" or direction == "s" or direction == "w"):
        return False
    elif x == 1 and y == 2 and (direction == "w"):
        return False
    elif x == 1 and y == 3 and (direction == "n" or direction == "w"):
        return False
    elif x == 2 and y == 1 and (direction == "e" or direction == "w" or direction == "s"):
        return False
    elif x == 2 and y == 2 and (direction == "n" or direction == "e"):
        return False
    elif x == 2 and y == 3 and (direction == "s" or direction == "n"):
        return False
    elif x == 3 and y == 2 and (direction == "w" or direction == "e"):
        return False
    elif x == 3 and y == 3 and (direction == "n" or direction == "e"):
        return False
    return True
def direction(x,y):
    direction_str=""
    if boundaries(x,y,"n"):
        direction_str= direction_str + "n"
    if boundaries(x,y,"e"):
        direction_str= direction_str + "e"
    if boundaries(x,y,"s"):
        direction_str= direction_str + "s"
    if boundaries(x,y,"w"):
        direction_str= direction_str + "w"

    return direction_str  
posx_int=1
posy_int=1
win_bool = False
while win_bool == False:

    directions_str=direction(posx_int,posy_int)
    travel_str = "You can travel: "
    
    for i in directions_str:
        
        if i == "n":
            travel_str = travel_str + "(N)orth"
        elif i == "e":
            travel_str = travel_str + "(E)ast"
        elif i == "s":
            travel_str = travel_str + "(S)outh"
        elif i == "w":
            travel_str = travel_str + "(W)est"
        if i != directions_str[len(directions_str)-1]:
            travel_str = travel_str + " or "
    print(travel_str + ".")

    next_pos = input('Direction: ').lower()
    if next_pos == 'n' and boundaries(posx_int,posy_int,next_pos):
        posy_int = north(posx_int,posy_int)
    elif next_pos == 'e' and boundaries(posx_int,posy_int,next_pos):
        posx_int = east(posx_int,posy_int)
    elif next_pos == 's' and boundaries(posx_int,posy_int,next_pos):
        posy_int = south(posx_int,posy_int)
    elif next_pos == 'w' and boundaries(posx_int,posy_int,next_pos):
        posx_int = west(posx_int,posy_int)
    else:
        print('Not a valid direction!')
    
    if posx_int == 3 and posy_int == 1:
        print("Victory!")
        break
