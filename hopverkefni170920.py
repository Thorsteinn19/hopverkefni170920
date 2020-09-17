
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
def boundaries(x,y):
    
    if 0 <x< 4 and 0< y <4:
        return True
    else:
        return False
def direction(x,y):
    direction_str=""
    if boundaries(x,north(x,y)):
        direction_str= direction_str + "n"
    if boundaries(x,south(x,y)):
        direction_str= direction_str + "s"
    if boundaries(west(x,y),y):
        direction_str= direction_str + "w"
    if boundaries(east(x,y),y):
        direction_str= direction_str + "e"
    return direction_str
    

#Skilgreina banngildisfærslur 
#1,1-2,1 ; 2,1 - 3,1 ; 2,2-3,2 ; 2,2 -2,3 ; færslur leifðar innan 1<= x,y <=3
posx_int=1
posy_int=1
win_bool = False
while win_bool == False:
    directions_str=direction(posx_int,posy_int)
    travel_str = "You can travel: "
    for i in directions_str:
        if i == "n":
            travel_str = travel_str + "(N)orth"
        elif i == "s":
            travel_str = travel_str + " or (S)outh"
        elif i == "e":
            travel_str = travel_str + " or (E)ast"
        elif i == "w":
            travel_str = travel_str + " or (W)est"
    print(travel_str)
    
