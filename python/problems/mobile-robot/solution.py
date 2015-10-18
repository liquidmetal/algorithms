# Complete the function below.

def go(posX, posY, orientation):
    if orientation == 0:
        posY -= 1
    elif orientation == 1:
        posX += 1
    elif orientation == 2:
        posY += 1
    elif orientation == 3:
        posX -= 1
    else:
        raise Exception("Unkonwn orientation")
        
    return (posX, posY)

def executeCommands(commands, times):
    posX = 0
    posY = 0
    orientation = 0
    for i in range(times):
        for c in commands:
            if c == 'G':
                (posX, posY) = go(posX, posY, orientation)
            elif c == 'L':
                orientation -= 1
                if orientation < 0:
                    orientation += 4
            elif c == 'R':
                orientation += 1
                if orientation > 3:
                    orientation -= 4

    return (posX, posY, orientation)
                

def  doesCircleExist( commands):
    (posX, posY, orientation) = executeCommands(commands, 4)
    return posX == 0 and posY == 0
