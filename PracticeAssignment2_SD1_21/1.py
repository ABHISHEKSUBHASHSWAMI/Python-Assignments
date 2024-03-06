#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#1 Write a program to check if a Substring is Present in a Given String.

main_str=str(input("Enter a string :"))
sub_str=str(input("Enter a substring :"))

if (main_str.find(sub_str)==-1):
    print("NO")
else:
    print("YES")