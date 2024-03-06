#Name : Abhishek Subhash Swami Roll No. 4
'''Write a function in Python to count the words "this" and "these" present in a text 
file "article.txt". [Note that the words "this" and "these" are complete words] '''

def counter():
    file=open('article.txt','r')
    para=file.read()
    words=para.split(' ')
    count1,count2=0,0
    for word in words:
        if word.lower()=='these':
            count1+=1
        elif word.lower()=='this':
            count2+=1
    print("Occurance of words\n'this': %d\n'these': %d" %(count2,count1))
    file.close()
counter()
