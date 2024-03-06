#Abhishek Subhash Swami Roll no. 4
'''Write a program to create function func1() to accept a variable length of arguments and 
print their value.
# call function with 3 arguments
func1(20, 40, 60)
# call function with 2 arguments
func1(80, 100)
Expected output:
Printing values
20
40
60
Printing values
80
10'''

def fun(*arg):
    print("Printing values")
    for i in arg:
        print(i)
fun(20,40,60)
fun(80,100)