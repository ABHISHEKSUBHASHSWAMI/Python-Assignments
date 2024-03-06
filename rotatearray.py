#program to rotate array

n=[]
numbers=[]
new=[]
num=input("Enter number separated by commas :")
numbers=num.split(",")
for i in numbers:
    n.append(int(i))
print(n)
k=int(input("Enter value for right shift :"))
l=len(n)-1
print(l)
if(k<l):
    new1=n[-k-1:l+1]
    new2=n[0:l-k+1]

print(new1 + new2)