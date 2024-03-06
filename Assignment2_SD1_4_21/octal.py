#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#Program to convert Decimal to Octal

num=int(input("Enter number :"))
octal=oct(num)
print(octal)

#looping solution
octal=[]

while(num):
    if(num>7):
        i=num%8
    else:
        i=num
    num=num//8
    octal.append(str(i))


print("0o"+"".join(octal[::-1]))