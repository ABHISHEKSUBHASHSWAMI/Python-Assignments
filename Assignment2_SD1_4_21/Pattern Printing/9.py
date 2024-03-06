#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#9 print numbers in triangular shape.

row=int(input("Enter number of rows: "))
initial=1

for i in range(0,row):
    for j in range(0,i+1):
        print(initial,end=" ")
        initial+=1
    print("")