#Abhishek Subhash Swami Roll no. 4
#Write a function that accept two numbers and returns addition, subtraction, 
#multiplication, division as a result(Return multiple values from a function)

def op(num1,num2):
    add=num1+num2
    sub=num1-num2
    pro=num1*num2
    div=num1/num2
    return (add,sub,pro,div)
a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
print(op(a,b))