#imports
import math
import numpy as np
from PIL import Image as im, ImageDraw as imdraw

# create array filled with white pixels 500x500, with the variables
# x is horizontal limit, y is vertical limit and d is the step between each line, in pixels
# w is the width of each line
print("input dimensions of image")
while True :
    try:
        x = int(input())
    except ValueError:
        print("Input an integer")
        
    else:
        break

while True :
    try:
        y = int(input())
    except ValueError:
        print("Input an integer")
        
    else:
        break
    
print("input step of first set of lines")
while True :
    try:
        d = int(input())
    except ValueError:
        print("Input an integer")
        
    else:
        break
    
print("input step of second set of lines")
while True :
    try:
        delta = int(input())
    except ValueError:
        print("Input an integer")
        
    else:
        break
        
#for testing
print("x= "+str(x))
print("y= "+str(y))
print("d= "+str(d))
print("delta= "+str(delta))
w = 3
a = -45*math.pi/180
array = np.full((y, x, 3), 
                        255, dtype = np.uint8) 

#prints the array
#print(array)

#saves the array into im format to be transformed into png
#draw will draw over original image, avec un reseau de lignes 
#NOTE the order is (x,y) so 0,250, 500,250 will draw a horizontal line of 500 pixels

data = im.fromarray (array)
draw = imdraw.Draw(data) 
#reseau de lignes #1
i = 0
while i<=x//d :
    draw.line((0+i*d,0 , 0+i*d,y), fill=0, width=w)
    i=i+1
    #if i==50:
        #break
#print ("End of loop #1")

data.save("reseau1.png")

#reseau de lignes #2
draw2 = imdraw.Draw(data)
n = 0
while n<=x//delta :
    draw2.line((y//math.tan(a)+n*delta,y , 0+n*delta,0), fill=0, width=w) 
    n=n+1
   # if n==100:
        #break
#print ("End of loop #2")

data.save("moire.png")
data.show()
#moire avec quelques zones d'interet qui ont ete surlignees
#trouver le ppcm
ppcm = math.lcm(d, delta)

draw3 = imdraw.Draw(data)
draw4 = imdraw.Draw(data)
#rouge = zone clair, vert = zone sombre
m=0
while m<=x//ppcm :
    draw3.line((m*ppcm,0 , m*ppcm,y), fill= (230, 0, 0), width=w)
    draw4.line((ppcm//2 + m*ppcm,0 , ppcm//2 + m*ppcm,y), fill=(0, 230, 0), width=w)
    m=m+1

data.save("zones.png")

#end message
print ("\nB)\n")
print ("!!! All done !!!\n")
print (":]\n")
