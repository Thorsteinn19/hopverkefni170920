#https://github.com/Thorsteinn19/hopverkefni170920
def where2go(x,y): #Skilgreinir hvert hægt sé að fara
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
def sentence_w2g(w2g): #Tekur gögn úr where2go og breytir því í setningu
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
def move(loc,x,y): #Framkvæmir færslu ef hún er lögleg
    if loc == 'n' and 'n' in where2go(x,y):
        y += 1
    if loc == 'e' and 'e' in where2go(x,y):
        x += 1
    if loc == 's' and 's' in where2go(x,y):
        y -= 1
    if loc == 'w' and 'w' in where2go(x,y):
        x -= 1
    return str(x)+str(y)
posx = 1
posy = 1
running = 1

while running == 1:
    print('You can travel: '+ sentence_w2g(where2go(posx,posy)))
    pos = input('Direction: ').lower()

    prevx = posx
    prevy = posy

    posx = int(move(pos,posx,posy)[0])
    posy = int(move(pos,posx,posy)[1])

    if posx == prevx and posy == prevy: #Ef færsla er ekki lögleg, lætur forritið vita
        print('Not a valid direction!')
   
    if posx == 3 and posy == 1: #Skilgreini vinningspunkt
        print('Victory!')
        break