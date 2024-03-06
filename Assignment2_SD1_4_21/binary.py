#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#program to convert decimal to binary

num=int(input("Enter number :"))
n=num
binary=[]
while(num>=1):
    i=num%2
    num=num//2
    binary.append(str(i))


print("0b"+"".join(binary[::-1]))

#or by built-in function
b=bin(n)
print(b)