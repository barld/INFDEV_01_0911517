
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
