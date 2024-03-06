#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#6 Python treats a string as special kind of tuple,if yes,prove it.

#Answer:Yes. Strings are special kind of tuples as once created cannot be changed until
#       you update it with new string. Tuples are also same. They are data structures which stores
#       ordered sequence of values. Tuples are also immutable.

string=str(input("Enter a string :"))

tuple1=tuple(string)

print(string)
print(tuple1)

print("From this we can say strings and tuples both return same sequenced data without changing it.")