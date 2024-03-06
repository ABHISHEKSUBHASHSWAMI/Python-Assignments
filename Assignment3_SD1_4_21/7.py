'''Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML
Concatinate two lists index wise'''

list1=["My","is"]
list2=["name","Abhishek"]
new=[]
for i in range(len(list1)):
	new.append(list1[i])
	new.append(list2[i])
print(" ".join(new))