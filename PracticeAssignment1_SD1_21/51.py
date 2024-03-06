#Name : Abhishek Subhash Swami Roll No. 21 AI-ML#29 
#51 Program to find factors of number in python

num=int(input("Enter a number :"))
factor=[]
for i in range(1,num+1):
    if(num%i==0):
        factor.append(str(i))
print("Factors are given as following :")
print(",".join(factor))