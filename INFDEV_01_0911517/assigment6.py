
def printSquare(height, width, full = False):
    figure = ""
    for i in range(0,height*width):        
        if i > 0 and i%width==0:
            figure += "\n"
        if full or i < width or i%width == 0 or i % width == width-1 or i > (height-1) * width:
            figure += "*"
        else:
            figure += " "

    print figure

printSquare(4,5,True)
printSquare(9,8,False)

def printRectangleTriangle(size):
    rectangle = ""
    for i in range(size+1):
        for j in range(i):
            rectangle += "*"
        rectangle += "\n"
    print rectangle

printRectangleTriangle(5)

def printIsoscelesTriangle(size):
    traingle = ""
    for i in range(size):
        for j in range(size*2-1):
            if size-2-i < j and (size-2-i)+((i+1)*2) > j:
                traingle += "*"
            else:
                traingle += " "

        traingle += "\n"
    print traingle

printIsoscelesTriangle(3)


import math

def printCircle(r):
    circle = ""
    for x in range(0,r*2+1):
        for y in range(0,r*2+1):
            if math.sqrt((x-r)**2 + (y-r)**2) < r:
                circle += "*"
            else:
                circle += "-"
        circle += "\n"

    print circle

def printSmiley(r):
    circle = ""
    for x in range(0,r*2+1):
        for y in range(0,r*2+1):
            if math.sqrt((x-r)**2 + (y-r)**2) < r:
                #eyes
                if (x == r/2 and y == r/2) or (x == r/2 and y == r + r/2):
                    circle += "O"
                #eyebrowes
                elif (x == r/2-1 and y == r/2) or (x == r/2-1 and y == r + r/2):
                    circle += "-"
                #mond
                elif x == r + r/2 and math.sqrt((x-r)**2 + (y-r)**2) < (r-2):
                    circle += "-"
                #nose
                elif x == r + r/4 and y == r:
                    circle += "#"
                elif math.sqrt((x-r)**2 + (y-r)**2) > r-1:
                    circle += "*"
                else:
                    circle += " "
            else:
                circle += " "
        circle += "\n"

    print circle

printCircle(15)

printSmiley(15)
printSmiley(10)
