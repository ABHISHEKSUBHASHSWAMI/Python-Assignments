'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
Given a Python list, remove all occurrence of 20 from the list
input:l1=[12,20,30,20]
output :=[12,30]'''

num=[]
newlst=[]
n=int(input("how many numbers? "))
for i in range(n):
	x=int(input("Enter number :"))
	num.append(x)
y=int(input("Enter number to be removed :"))
for i in range(n):
	if(num[i]!=y):
		newlst.append(num[i])
print(newlst)
