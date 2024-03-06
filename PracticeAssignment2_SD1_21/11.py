#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#11 Write a Python program to count the character frequency in a string


def start():
   
    opt=int(input("Enter 1 or 2 to choose method :"))
    if(opt==1):
        count=string.count(char)
        print(count)
    elif(opt==2):
        count=0
        for i in string:
            if(i==char):
                count=count+1
            else:
                count=count+0
        print("Character occured",count,"times")
    else:
        print("Incorrect option")
        start()
 
string=str(input("Enter a string :"))
char=str(input("Enter character to calculate frequency :"))
start()

