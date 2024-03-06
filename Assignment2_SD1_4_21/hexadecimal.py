#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#Program to convert decimal to hexadecimal

num=int(input("Enter a number :"))
hexadecimal=hex(num)
print(hexadecimal)

#looping solution
hex=[]
while(num):
    if(num<0):
        hex.append("0")
    elif(num<=1):
        hex.append(str(num))
    else:
        x =(num%16)
        if (x < 10):
            hex.append(str(x) )
        if (x == 10):
            hex.append("A")
        if (x == 11):
            hex.append("B")
        if (x == 12):
            hex.append("C")
        if (x == 13):
            hex.append("D")
        if (x == 14):
            hex.append("E")
        if (x == 15):
            hex.append ("F")
        num=num//16

print("0x"+"".join(hex[::-1]))