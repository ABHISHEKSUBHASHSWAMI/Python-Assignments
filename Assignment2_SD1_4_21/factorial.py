#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#Find factorial of number in python

n=int(input("Enter number to calculate factorial :"))
factorial=1
num=str(n)
if(n<0):
    print("Factorial doesn't exist!")
else:
    while(n):
        factorial=factorial*n
        n=n-1
    print("\n",num,"!=",factorial,"\n")