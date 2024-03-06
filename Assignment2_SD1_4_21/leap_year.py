#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#Program to Check Leap Year in python.

year=int(input("Enter a year :"))

if(year%4==0):
    print("This is a leap year.")
else:
    print("This is not a leap year. Next leap year is",4-(year%4),"years away, i.e.",(year+4-(year%4)))
