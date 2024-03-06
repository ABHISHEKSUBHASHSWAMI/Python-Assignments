#Abhishek Subhash Swami Roll no. 4
#WAP to add,delete and update an item in a tuple

tup=(5,6,5,9,6,8,65,6,4,7,5,55,8,5,8,5,6,6,8,255,2,99,5,56,3,5)

ltup=list(tup)
#update
n=int(input("Enter element to be updated :"))
n_index=int(input("Enter index value to be updated :"))
ltup[n_index]=n

#add
new=int(input("Enter element to be added :"))
ltup.append(new)

#remove or delete item (only first occurance)
rm=int(input("which element you want to delete:"))
ltup.remove(rm)

newtup=tuple(ltup)
print(newtup)