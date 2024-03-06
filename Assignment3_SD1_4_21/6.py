'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
6.Python program to find first and second largest number in a list
Input: list1=[2,4,10,1]
Output=1,2'''

num=[]
newlst=[]
n=int(input("how many numbers? "))
for i in range(n):
	x=int(input("Enter number :"))
	num.append(x)
newlst=sorted(num)
print(newlst[-1:-3:-1])
