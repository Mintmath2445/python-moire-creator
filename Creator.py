
#selection of which moire
import os
print("which moire type? Select number")
list = ["1. Lines", "2. Circles", "3. Angles"]
print(list)
while True:
    try:
        choice = int(input())
        if (choice > 3) and (choice < 1):
            print("input one the numbers given")
            print(list)
            check = False
        else:
            check = True
            break
        
    except ValueError:
        print("input one the numbers given")
        print(list)
    if check != False:
        check = False
        break
if choice == 1:
    open("Line.py")
if choice == 2:
    open("Circles.py")
if choice == 3:
    open("Angle.py")
    
        
    

       
