#Name : Abhishek Subhash Swami Roll No. 4
'''Write a function in Python to count words in a text file those are ending with 
alphabet "e".'''

def counter():
    file=open('article.txt','r')
    data=file.read()
    words=data.split(' ')
    count=0
    for word in words:
        if word[-1]=='e':
            count+=1
    print(count)
    file.close()
counter()
