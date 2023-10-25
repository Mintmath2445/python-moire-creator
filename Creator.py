
#selection of which moire
import os
print("which moire type? Select number")
list = ["1. Lines", "2. Circles", "3. Angles"]
print(list)
while True:
    try:
        choice = int(input())
        if (choice > 3) or (choice < 1):
            print("input one the numbers given")
            print(list)
            check = False
        else:
            check = True
            break
        
    except ValueError:
        print("input one the numbers given")
        print(list)
        check = False
    if check != False:
        check = False
        break
if choice == 1:
    with open("Line.py", 'r') as file:
         python_code = file.read()
         exec(python_code)
if choice == 2:
    with open("Circles.py", 'r') as file:
         python_code = file.read()
         exec(python_code)
#if choice == 3:
    #open("Angle.py")
else:
    print("Oops, an error has occured, :C")
    exit(-1)
exit(0)