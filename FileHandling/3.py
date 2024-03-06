# Name: Abhishek Subhash Swami Roll No. 4
'''Write a function in Python to count and display the total number of words in a text 
file'''

def word_count():
    file=open('story.txt','r')
    count=0
    for each in file:
        words=each.split(' ')
        count+=len(words)
    file.close()
    print('Total Words are',count)
word_count()