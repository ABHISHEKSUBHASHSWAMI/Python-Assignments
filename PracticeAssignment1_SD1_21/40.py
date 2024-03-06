#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#40 Program to check number is Prime or not.

def prime(n):
    mark=0
    for i in range(2,(n//2)+1):
        if (n%i==0):
            mark=1
            print("Not a Prime Number.")
            break
    if (mark==0):
        print("Prime Number.")
    

number=int(input("Enter a number :"))
prime(number)