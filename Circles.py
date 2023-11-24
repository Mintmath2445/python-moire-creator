
#imports
import os
import math
import numpy as np
from PIL import Image as im
import drawsvg as draw

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
    
print("input distance between circles")    
while True :
    try:
        dist = int(input())
        if dist > x:
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

#array = np.full((y, x, 3), 
                        #255, dtype = np.uint8) 

#prints the array
#print(array)

#saves the array into im format to be transformed into png
#draw will draw over original image, avec un reseau de lignes 
#NOTE the order is (x,y) so 0,250, 500,250 will draw a horizontal line of 500 pixels

data = draw.Drawing(x, y, origin= (0, 0))
 
#cercle 1
i = 0
while i<=x//d :
    data.append(draw.Circle(x/2-dist/2,y/2,d*i, fill= "none", stroke_width = w, stroke = "black"))
    i=i+1
    #if i==50:
        #break
#print ("End of loop #1")

data.set_pixel_scale(1)
data.save_svg("cercle1.svg")

#cercle 2
n = 0
while n<=x//delta :
    data.append(draw.Circle(x/2+dist/2,y/2,delta*n, fill= "none", stroke_width = w, stroke = "black"))
    n=n+1
    
data.save_svg("moirecercle.svg")
#data.show()
#moire avec quelques zones d'interet qui ont ete surlignees

#bleu = zone claire, vert = zone sombre
m=0
#while m<=x//d :
    #draw.line(0, y/2, x/3, )

#data.save("zonescercle.png")

#end message
print ("\nB)\n")
print ("!!! All done !!!\n")
print (":]\n")
exit(0)