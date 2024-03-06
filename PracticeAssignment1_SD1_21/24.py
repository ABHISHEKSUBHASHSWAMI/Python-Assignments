#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#24 Program to solve a quadratic equation in python.
import math
print("General quadratic equation is given as aX^2 + bX + c = 0")

a=int(input("Enter value for coefficient of X^2 with + or - sign :"))
b=int(input("Enter value for coeficient of X with + or - sign :"))
c=int(input("Enter value of constant with + or - sign :"))

root1=(-b + math.sqrt((b**2) - (4*a*c)))/2*a
root2=(-b - math.sqrt((b**2) - (4*a*c)))/2*a

print("Root of equation is",root1,"or",root2)