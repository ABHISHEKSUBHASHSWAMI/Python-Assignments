#Name: Abhishek Subhash Swami Roll No. 4
#Write a program to open a file and read data

def rfile():
    file=open('poem.txt','r')
    for each in file:
        print(each)
    file.close()
rfile()