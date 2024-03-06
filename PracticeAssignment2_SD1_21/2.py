#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#2 Write a program in python to check if two strings are anagram or not.

str1=str(input("Enter first string :"))
str2=str(input("Enter second string :"))

str3=sorted(str1)
str4=sorted(str2)

if(str3==str4):
    print("These strings are anagram.")
else:
    print("These strings are not anagram.")

print(sorted(str1))