#Abhishek Subhash Swami Roll no. 4
#Write a Python program calculate the product, multiplying all the numbers of a given tuple.

tup=(1,4,5,6,8,44,5,6,7,8,9)
product=1
for i in range(len(tup)):
    product=product*tup[i]
print(product)