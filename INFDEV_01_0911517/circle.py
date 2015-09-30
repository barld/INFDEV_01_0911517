import math

r=60
coordinates = [(int(r*math.cos(i)), int(r*math.sin(i))) for i in range(0,361,1)]

block = [[" " for j in range(-r,r+1)] for i in range(-r,r+1)]
        
for (x,y) in coordinates:
    block[x+r][y+r] = "*"

for row in block:
    line = ""
    for cell in row:
        line += cell
    print line