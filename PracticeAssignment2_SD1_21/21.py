#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#21 Write a Python program to remove a newline in Python
#method 1
temp=["cat\n","dog\n","cow\n","goat\n"]
new_list=[]
for i in temp:
    new_list.append(i.replace("\n",""))
print("string before :",temp)
print("string after :",new_list)

#method 2
string="\nMy name is Abhishek Subhash Swami\n"

new_string=string.rstrip()

print("string before :\n",string)
print("string after removing newline :",new_string)