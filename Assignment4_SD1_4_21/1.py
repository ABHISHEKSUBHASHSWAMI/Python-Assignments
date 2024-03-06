#Abhishek Subhash Swami Roll no. 4
#Write a program to count repeated items in tuples

tup=(1,1,4,6,4,7,8,4,6,2,1,3,5,7,8,9,4)
for i in range(len(tup)):
    count=tup.count(tup[i])
    print(tup[i],":",count)
