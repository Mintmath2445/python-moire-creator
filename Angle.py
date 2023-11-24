#imports
import os
import math
import numpy as np
from PIL import Image as im
import drawsvg as draw

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
#the angle will be 90-angle, but the input will be close to 0, without it being 0    
print("input angle in degrees")    
while True :
    try:
        angle = int(input())
        if angle > 180 and angle == 90:
            print("Too large or angle = 90")
            didpass = False
        else:
            didpass = True
    except ValueError:
        print("Input an integer")
        
    if didpass !=False:
        a = math.pi*(angle/180)
        arad = math.pi*((90-angle)/180)
        didpass = False
        break     
     
print("input step of second set of lines")
while True :
    try:
        delta = int(input())/math.sin(arad)
        if delta > x :
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
print("a = "+str(a))

data = draw.Drawing(x, y, origin= (0, 0))
 
#lignes 1
i = 0
while i<=x//d :
    data.append(draw.Line(d*i,y,d*i,0, fill= "none", stroke_width = w, stroke = "black"))
    i=i+1
    #if i==50:
        #break
#print ("End of loop #1")

data.set_pixel_scale(1)
data.save_svg("angle1.svg")

#plan de lignes 2
n = 0
while n<=x//delta :
    data.append(draw.Line(delta*n,y,y/math.tan(arad)+delta*n,0, fill= "none", stroke_width = w, stroke = "black"))
    n=n+1
    
data.save_svg("moireangle.svg")
#data.show()
#moire avec quelques zones d'interet qui ont ete surlignees

#bleu = zone claire, vert = zone sombre
m=0
while m<=x//d :
    data.append(draw.Line(0, y-m*(-d*((d-delta)*math.tan(arad)/d)+d*math.tan(arad)), x, y-((x-d)*(((d-delta)*math.tan(arad))/d)+m*d*math.tan(arad)), fill= "none", stroke_width = 2, stroke = "blue"))
    data.append(draw.Line(0, y-m*(-d*((d-delta)*math.tan(arad)/d)+d*math.tan(arad))-d*math.tan(arad)/2, x, y-((x-d)*(((d-delta)*math.tan(arad))/d)+m*d*math.tan(arad))-d*math.tan(arad)/2, fill= "none", stroke_width = 2, stroke = "green"))
    m=m+1

data.save_svg("zonesangle.svg")

#end message
print ("\nB)\n")
print ("!!! All done !!!\n")
print (":]\n")
exit(0)
      