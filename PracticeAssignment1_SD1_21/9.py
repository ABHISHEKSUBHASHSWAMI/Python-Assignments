#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#9 Median of numbers

n=int(input("How many numbers are there)? :"))
count=0
list=[]
while(count<n):
    num=int(input("Enter Number :"))
    count=count+1
    list.append(num)

sorted_num=sorted(list)
x=len(sorted_num)
if x % 2 == 0:
    median1 = sorted_num[x//2]
    median2 = sorted_num[x//2 - 1]
    median = (median1 + median2)/2
else:
    median = sorted_num[n//2]

print("Median is ",median)