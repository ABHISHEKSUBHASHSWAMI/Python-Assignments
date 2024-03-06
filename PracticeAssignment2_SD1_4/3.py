#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#3 Write a program in python to count and display vowels in a string.

string=str(input("Enter a string :"))
vowels=list("AaEeIiOoUu")
check=[each for each in string if each in vowels]

print(len(check))
print(check)