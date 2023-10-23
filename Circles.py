
#imports
import os
import math
import numpy as np
from PIL import Image as im, ImageDraw as imdraw

# create array filled with white pixels 500x500, with the variables
# x is horizontal limit, y is vertical limit and d is the step between each line, in pixels
# w is the width of each line
# didpass is a checking variable for try loops
didpass = False
print("input dimensions of image")
while True :
    try:
        x = int(input())
        if x > 4096:
            print("Too large")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        didpass = False
        break
    
while True :
    try:
        y = int(input())
        if y > 4096:
            print("Too large")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        didpass = False
        break
    
print("input step of first set of lines")
while True :
    try:
        d = int(input())
        if d > x:
            print("Too large")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        didpass = False
        break
    
print("input step of second set of lines")
while True :
    try:
        delta = int(input())
        if delta > x:
            print("Too large")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        didpass = False
        break
    
print("input width of lines")
while True :
    try:
        w = int(input())
        if w > d:
            print("Too large")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        didpass = False
        break
          
#for testing
print("x = "+str(x))
print("y = "+str(y))
print("d = "+str(d))
print("delta = "+str(delta))
print("w = "+str(w))

array = np.full((y, x, 3), 
                        255, dtype = np.uint8) 

#prints the array
#print(array)

#saves the array into im format to be transformed into png
#draw will draw over original image, avec un reseau de lignes 
#NOTE the order is (x,y) so 0,250, 500,250 will draw a horizontal line of 500 pixels

data = im.fromarray (array)
draw = imdraw.Draw(data)
 
#cercle 1
i = 0
while i<=x//d :
    draw.line((0+i*d,0 , 0+i*d,y), fill=0, width=w)
    i=i+1
    #if i==50:
        #break
#print ("End of loop #1")

data.save("cercle1.png")

#cercle 2

data.save("moirecercle.png")
data.show()
#moire avec quelques zones d'interet qui ont ete surlignees

#rouge = zone sombre???, vert = zone sombre




#end message
print ("\nB)\n")
print ("!!! All done !!!\n")
print (":]\n")
