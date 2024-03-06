#Name : Abhishek Subhash Swami Roll No. 4(21) AI-ML

#1 WAP Count occurrences of an element in a list
#Input= lst = [15, 6, 7, 10, 12, 20, 10, 28, 10, 12, 52, 6, 2]
#x = 10
#Output : 3 


count=0
lst=[15, 6, 7, 10, 12, 20, 10, 28, 10, 12, 52, 6, 2]
num=int(input("Enter number to calculate frequency of a number :"))
for i in range(len(lst)):
	if(lst[i]==num):
		count+=1
print(num,"has occured in given list for",count,"times")
	
