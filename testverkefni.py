x = 1
y = 1
nice = 1

while nice == 1:
    pos = input('input direction: ').lower()
    if pos == 'n':
        y = north(y)
    elif pos == 's':
        y = south(y)
    elif pos == 'e':
        x = east(x)
    elif pos == 'w':
        x = west(x)
    else:
        print('Invalid')
    print(x,y)