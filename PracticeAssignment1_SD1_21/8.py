#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#8 Mean of numbers

n=int(input("how many numbers are there? "))
sum=0
count=1

while(count<=n):
    number=int(input("Enter number: "))
    sum=sum+number
    count=count+1
mean=sum/n

print(round(mean,2))
