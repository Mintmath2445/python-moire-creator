
#imports
import os
import math
import numpy as np
from PIL import Image as im, ImageDraw as imdraw

# create array filled with white pixels 500x500, with the variables
# x is horizontal limit, y is vertical limit and d is the step between each line, in pixels
# w is the width of each line
# didpass is a checking variable for try loops
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
    
print("want an angle?")
print("Y or N")
answer = input()
yesses = ["Y","y","YES","yES","Yes", "yes"]
noes = ["N", "n", "no", "NO", "nO", "No"]
while True:
    if answer in yesses:
        print("input angle")
        while True :
            try:
                a = float(input())*math.pi/180
                break
            except ValueError:
                print("Input a real")
        break
    elif answer in noes:
        a = 0
        break
    else:
        print("Y or N")
        answer = input()
      
#for testing
print("PPCM = "+str(math.lcm(d,delta)))
print("x = "+str(x))
print("y = "+str(y))
print("d = "+str(d))
print("delta = "+str(delta))
print("w = "+str(w))
print("angle = "+str(a*180/math.pi))
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
    try:
        draw2.line((y//math.tan(a)+n*delta,0 , 0+n*delta,y), fill=0, width=w) 
        n=n+1
    except ZeroDivisionError:
        draw2.line((n*delta,0 , n*delta,y), fill=0, width=w) 
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
#bleu = zone clair, vert = zone sombre
m=0
while m<=x//ppcm :
    draw3.line((m*ppcm,0 , m*ppcm,y), fill= (0, 0, 255), width=w)
    draw4.line((ppcm//2 + m*ppcm,0 , ppcm//2 + m*ppcm,y), fill=(0, 255, 0), width=w)
    m=m+1

data.save("zones.png")

#end message
print ("\nB)\n")
print ("!!! All done !!!\n")
print (":]\n")
