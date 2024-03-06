'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
Input: l1=[1,2,3]
L2:[4,5,6]
Output:[1,2,3,6,5,4]'''

lst1=[]
lst2=[]
n1=int(input("how many numbers you want to enter in list 1:"))
n2=int(input("how many numbers you want to enter in list 2:"))
print("Enter number for list 1 :")
for i in range(n1):
	x=int(input("Enter number :"))
	lst1.append(x)
print("Enter numbers for list 2 :")
for i in range(n2):
	y=int(input("Enter number :"))
	lst2.append(y)
print(lst1+lst2[::-1])
