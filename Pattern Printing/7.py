#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#7 print triangle out of numbers.

num=int(input("Enter number of rows: "))

for i in range(1,num+1):
    for j in range(i):
        print(j+1,end=" ")
    print("")