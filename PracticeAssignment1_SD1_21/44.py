#Name : Abhishek Subhash Swami Roll No. 21 AI-ML#29 
#44 Program to print multiplication table of given number

number=int(input("Enter a number to print table :"))
print("Multiplication table for",number,"is :")
for i in range(1,11):
    mult=number*i
    print(number,"x",i,"=",mult)