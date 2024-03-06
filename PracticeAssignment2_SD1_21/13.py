#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#13 Write a Python program to remove the nthindex character from a nonempty str.

string=str(input("Enter a String :"))
value=int(input("Enter index number for character to be removed from string :"))

part1=string[:value]
part2=string[value+1:]
new_string=part1+part2
print(new_string)