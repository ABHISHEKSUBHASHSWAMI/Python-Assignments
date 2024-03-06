#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#Write a program to check if string is palindrome or not.

string=str(input("Enter string to check :"))

if string[::]==string[::-1]:
    print("It's Palindrome.")
else:
    print("It's not a palindrome.")