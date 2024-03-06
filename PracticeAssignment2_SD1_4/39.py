#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#39 Write a program that asks the user to enter a string.
#The program should then print the following:
# a.The total number of characters in the string
# b.The string repeated 10 times
# c.The first character of the string (remember that string indices start at 0)
# d.The first three characters of the string
# e.The last three characters of the string
# f.The string backwards
# g.The string with its first and last characters removed
# h.The string in all caps
# i.The string with every a replaced with an e
# j.The string with every letter replaced by a space

string=str(input("Enter a string :"))
print(len(string))
n=10
while(n>0):
    print(string)
    n-=1
print("First character is :",string[0:1])
print("First three characters are :",string[0:3])
print("Backward string is :",string[::-1])
print("First & last letter removed string :",string[1:-1])
print("String in upper case is :",string.upper())
print("Every a replaced by e in string :",string.replace("a","e"))
print("Every letter in string replaced by space :"," "*len(string))

