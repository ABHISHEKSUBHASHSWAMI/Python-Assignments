#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#41 Write a program that asks the user to enter two strings of the same length.
#The program should then check to see if the strings are of the same length.
#If they are not, the program should print an appropriate message and exit.
#If they are of the same length, the program should alternate the characters of the two strings.
#For example, if the user enters xyz and ABCthe program should print out AxByCz.

print("Enter two strings of same length :")
string1=str(input("Enter first string :"))
string2=str(input("Enter second string :"))
string=[]
if(len(string1)!=len(string2)):
    print("Given strings are not of same length.")
else:
    for i in range(0,len(string1)):
        string.append(string1[i]+string2[i])
    print("".join(string))