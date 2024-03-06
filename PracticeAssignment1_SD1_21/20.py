#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#20 Program to calculate total surface area of a cylinder in Python

import math
radius=float(input("Enter radius of cylinder :"))
height=float(input("Enter height of cylinder :"))
unit=str(input("Enter unit :"))

surface_area= 2*math.pi*(pow(radius,2)+(radius*height))

print("Surface area=",round(surface_area,2),"square",unit,)