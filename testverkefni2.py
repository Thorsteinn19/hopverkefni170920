#https://github.com/Thorsteinn19/hopverkefni170920

def where_to_go(x,y): 
    '''
    Tekur inn staðsetningu leikmanns
    Skilar út mögulegum áttum sem má fara í.
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

def sentence_w_to_g(where_to_go_str): 
    '''
    Tekur niðurstöðu where_to_go fallsins
    Skilar út heilsteyptri setningu á ensku
    '''
    possible_directions_str = ''
    for i in where_to_go_str:

        if i == 'n':
            possible_directions_str = '(N)orth'

        elif i == 'e':
            possible_directions_str = possible_directions_str + '(E)ast'

        elif i == 's':
            possible_directions_str = possible_directions_str + '(S)outh'

        elif i == 'w':
            possible_directions_str = possible_directions_str + '(W)est'

        if i != where_to_go_str[len(where_to_go_str)-1]:
            possible_directions_str = possible_directions_str + ' or ' 

    possible_directions_str = possible_directions_str + '.'
    
    return possible_directions_str

def move(direction,x,y):
    '''
    Les inn staðsetningu og hvert leikmaður vill fara
    Framkvæmir færslu ef hún er lögleg
    '''
    if direction == 'n' and 'n' in where_to_go(x,y):
        y += 1

    if direction == 'e' and 'e' in where_to_go(x,y):
        x += 1

    if direction == 's' and 's' in where_to_go(x,y):
        y -= 1

    if direction == 'w' and 'w' in where_to_go(x,y):
        x -= 1

    return str(x)+str(y)

x_position_int = 1
y_position_int = 1
running_bool = True

while running_bool:
    print('You can travel: '+ \
        sentence_w_to_g(where_to_go(x_position_int,y_position_int)))

    next_direction_str = input('Direction: ').lower()

    previous_x = x_position_int
    previous_y = y_position_int

    x_position_int = int(move(next_direction_str,x_position_int,y_position_int)[0])
    y_position_int = int(move(next_direction_str,x_position_int,y_position_int)[1])

    #Ef færsla er ekki lögleg og leikmaður var ekki færður, lætur forritið vita
    if x_position_int == previous_x and y_position_int == previous_y: 
        print('Not a valid direction!')
   
    #Skilgreini vinningspunkt
    if x_position_int == 3 and y_position_int == 1:
        print('Victory!')
        break