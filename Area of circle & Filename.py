#WAP to accepts the radius of a circle from the user and compute area.

import math
radius = float(input("Input the radius of the circle : "))
area = math.pi*radius*radius
print("The area of the circle with radius", radius, "is:", area)


#WAP to accept a filename from the user and print the extension of that.

file_name = input("Input the Filename : ")
file_extns = file_name.split(".")
if (file_extns[-1] == 'py'):
    print("The extension of the file is :", 'python')
else :
    print("The extension of the file is :", file_extns[-1])
