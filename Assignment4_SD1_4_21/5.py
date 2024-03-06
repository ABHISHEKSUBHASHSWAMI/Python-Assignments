#Abhishek Subhash Swami Roll no. 4
#WAP to add, delete and update an item in a set

set1={4,6,"happy"}

#add to set
a=input("Enter element to  be added to set :")
set1.add(a)
print(set1)

#delete set items
b=input("Enter element to be deleted :")
set1.discard(b)

#update set
set2={"hello",45}
set1.update(set2)

print(set1)