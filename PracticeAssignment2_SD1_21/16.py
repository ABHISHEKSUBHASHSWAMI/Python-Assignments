#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#16 Write a Python program to remove the characters which have odd index values of a given string

string=str(input("Enter a string :"))

new=""
for i in range (len(string)):
    if i%2==0:
        new=new+string[i]

print(new)