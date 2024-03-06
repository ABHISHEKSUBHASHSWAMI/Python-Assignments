#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#Program to print sum of n natural numbers

number=int(input("Enter number :"))
sum=0
#using for loop

for i in range(1,number+1):
    sum=sum+i

print("Sum is",sum)

#using while loop
wsum=0
while(number):
    wsum+=number
    number-=1
print("Sum is",wsum)
