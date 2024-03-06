#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#15-16 HCF of two numbers in python

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
list=[]
for i in range(2,num1):
    if num1%i==0 and num2%i==0:
        list.append(i)
print(list[-1]," is HCF.")

#16 LCM of two numbers
LCM=int((num1*num2)/list[-1])
print(LCM, "is LCM.")