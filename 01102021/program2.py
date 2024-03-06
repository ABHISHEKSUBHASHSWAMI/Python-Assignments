#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

'''Write a Python program to accept the useer's first name and last name and then getting them printed
in reverse order with a space between first name and last name.'''

first_name=input(str("Enter your first name :"))
last_name=input(str("Enter your last name :"))

print(last_name[::-1],first_name[::-1])