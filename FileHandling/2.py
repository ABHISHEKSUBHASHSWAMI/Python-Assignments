#Name: Abhishek Subhash Swami Roll No. 4
'''Write a function in python to count the number of lines
from a text file "story.txt" which is not starting with an alphabet "T"'''

def storylinecount():
    story=open('story.txt','r')
    count=0
    for line in story:
        if line[0] not in 'T':
            count+= 1
    story.close()
    print("No of lines not starting with 'T'=",count)
storylinecount()