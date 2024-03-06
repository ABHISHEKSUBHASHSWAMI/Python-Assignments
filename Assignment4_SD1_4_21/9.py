#Abhishek Subhash Swami Roll no. 4
#Write a Python program to sum ,multiply all the items in a dictionary

data={"var1":45, "var2":12, "var3":5, "var4":7, "var5":3}
sum=0 ; product=1
for i in data:
    sum=sum+data[i]
    product=product*data[i]
print("Sum :",sum,"\nProduct :",product)