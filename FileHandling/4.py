# Name : Abhishek Subhash Swami Roll No. 4
''' Write a function in Python to read lines from a text file "story.txt". Your function 
should find and display the occurrence of the word "the" '''

def the_count():
    file=open('notes.txt','r')
    count=0
    data = file.read()
    words = data.split()
    for word in words:
        if word.lower()=="the":
            count += 1
    file.close()
    print(count)
the_count()