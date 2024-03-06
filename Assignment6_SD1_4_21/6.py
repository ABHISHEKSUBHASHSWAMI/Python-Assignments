# Write a Python function to sum all the numbers in a list.

def add(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    return sum
num=[45,15,65,35,2,55,8,69,56,58,23,22]

print(add(num))