#Abhishek Subhash Swami Roll no. 4
#WAP to perform union, intersection, symmetric difference an item in a set

S={"hello",22,1,4,5,9,"green","yellow"}
A={22,5,"new","u","hello"}

#union
B=S.union(A)
print("S U A =",B)

#intersection
C=S.intersection(A)
print("S ∩ A =",C)

#symmetrical difference
D=S.symmetric_difference(A)
print("Symmetric Difference :",D)