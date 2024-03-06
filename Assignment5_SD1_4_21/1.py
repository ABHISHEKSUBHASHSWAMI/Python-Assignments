#Abhishek Subhash Swami Roll no. 4
#Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent 
#class and function to calculate the area should be defined in subclass

class triangle:
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
class A(triangle):
    def area(self):
        s=(self.s1 + self.s2 + self.s3)/2
        return (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**(0.5)

a=int(input("Enter side 1 :"))
b=int(input("Enter side 2 :"))
c=int(input("Enter side 3 :"))

new_tringle=A(a,b,c)
print("Area of triangle :",new_tringle.area())
