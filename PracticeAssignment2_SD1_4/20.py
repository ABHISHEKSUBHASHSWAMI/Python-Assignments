#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#20 Write a Python program to sort a string lexicographically.

string=str(input("Enter a string :"))
string1=string.lower()
words=string1.split()
words.sort()
for i in words:
    print(i)
