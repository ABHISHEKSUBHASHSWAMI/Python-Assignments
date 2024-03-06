'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
Given a Python list of numbers. Turn every item of a list into its square
Input:l1=[1,2,3,4]
Output:[1,4,9,16]'''
num=[]
sqr=[]
n=int(input("How many numbers ? "))
print("Enter numbers in list :")
for i in range(n):
	x=int(input("Enter number :"))
	num.append(x)
for i in range(n):
	s=num[i]**2
	sqr.append(s)
print(sqr)
