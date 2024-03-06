#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

'''1. Write a program which will find numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma separated sequence on a single line'''

numbers=[]
for i in range(2000, 3201):
    if (i%7==0 and i%5!=0):
        numbers.append(str(i))
print(','.join(numbers))


'''2. Write a Python program to accept the useer's first name and last name and then getting them printed
in reverse order with a space between first name and last name.'''

first_name=str(input("Enter your first name :"))
last_name=str(input("Enter your last name :"))

print(last_name[::-1],first_name[::-1])


'''3. Write a program to calculate volume of sphere with diameter 12cm: Formula is V=4/3 * pi * r**3'''

import math
diameter=12
unit=str('cm')
radius=diameter/2
volume=(4/3)*(math.pi)*(pow(radius, 3))

print("Volume of Sphere =",'%0.2f'%volume)
