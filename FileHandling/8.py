#Name : Abhishek Subhash Swami Roll No. 4
'''Write a function in Python to count uppercase character in a text file.'''

def uppercounter():
    file=open('poem.txt', 'r')
    words=file.read()
    count=0
    for letter in words:
        if letter.isupper():
            count+=1
    print(count)
    file.close()
uppercounter()