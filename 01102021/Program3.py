#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

'''Write a program to calculate volume of sphere with diameter 12cm: Formula is V=4/3 * pi * r**3'''

import math
diameter=12
unit=str('cm')
radius=diameter/2
volume=(4/3)*(math.pi)*(pow(radius, 3))

print("Volume of Sphere =",'%0.2f'%volume)