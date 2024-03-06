#Write a Python function to find the Max of three numbers.

def max(a,b,c):
    if(a>b and a>c):
        max=a
    elif(b>c):
        max=b
    else:
        max=c
    return max
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

print("maximun numbere is :",max(num1,num2,num3))