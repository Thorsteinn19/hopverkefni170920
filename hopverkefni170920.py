
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

    

#Skilgreina banngildisfærslur 
#1,1-2,1 ; 2,1 - 3,1 ; 2,2-3,2 ; 2,2 -2,3 ; færslur leifðar innan 1<= x,y <=3
print(boundaries(3,north(3,3)))