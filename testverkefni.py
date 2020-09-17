#https://github.com/Thorsteinn19/hopverkefni170920
def where2go(x,y):
    '''
    Skilgreinir hver hægt sé að fara
    '''
    if x == 1 and y == 1:
        possible = 'n'
    elif x == 1 and y == 2:
        possible = 'nes'
    elif x == 1 and y == 3:
        possible = 'es'
    elif x == 2 and y == 1:
        possible = 'n'
    elif x == 2 and y == 2:
        possible = 'sw'
    elif x == 2 and y == 3:
        possible = 'ew'
    elif x == 3 and y == 2:
        possible = 'ns'
    elif x == 3 and y == 3:
        possible = 'sw'
    return possible
def sentence(w2g): 
    '''
    Tekur gögn úr where2go og breytir því í setningu
    '''
    string = ''
    for i in w2g:
        if i == 'n':
            string = '(N)orth'
        elif i == 'e':
            string = string + '(E)ast'
        elif i == 's':
            string = string + '(S)outh'
        elif i == 'w':
            string = string + '(W)est'
        if i != w2g[len(w2g)-1]:
            string = string + ' or ' 
    string = string + '.'
    return string
def move(direction,x,y):
    '''
    Framkvæmir færslu ef hún er lögleg
    '''
    if direction == 'n' and 'n' in where2go(x,y):
        y += 1
    if direction == 'e' and 'e' in where2go(x,y):
        x += 1
    if direction == 's' and 's' in where2go(x,y):
        y -= 1
    if direction == 'w' and 'w' in where2go(x,y):
        x -= 1
    return str(x)+str(y)

posX = 1
posY = 1
running = 1

while running == 1:
    print('You can travel: '+ sentence(where2go(posX,posY)))
    moveInp = input('Direction: ').lower()

    prevX = posX
    prevY = posY

    posX = int(move(moveInp,posX,posY)[0])
    posY = int(move(moveInp,posX,posY)[1])

    #Ef færsla er ólögleg, lætur forritið vita
    if posX == prevX and posY == prevY: 
        print('Not a valid direction!')
   
   #Skilgreini vinningspunkt
    if posX == 3 and posY == 1:
        print('Victory!')
        break