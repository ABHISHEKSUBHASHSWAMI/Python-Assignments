'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
Given a list, print the value obtained after multiplying all numbers in a list. 
Examples: 
Input :  list1 = [1, 2, 3] 
Output : 6 
Explanation: 1*2*3=6'''

num=[]
product=1
n=int(input("how many numbers you want to enter:"))
for i in range(n):
	x=int(input("Enter number :"))
	num.append(x)
for i in range(n):
	product*=num[i]
print(product)
