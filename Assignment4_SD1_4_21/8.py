#Abhishek Subhash Swami Roll no. 4
#WAP to generate and print a dictionary that contains
#a number (between 1 and n) in the form (x, x*x).

num=int(input("Enter a number :"))
square={}
for i in range(1,num+1):
    square[i]=i*i
print(square)