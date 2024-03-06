#Name : Abhishek Subhash Swami Roll No. 4
'''Write a function display_words() in python to read lines from a text file "story.txt", 
and display those words, which are less than 4 characters.'''

def display_words():
    file=open('story.txt','r')
    para=file.read()
    words=para.split(' ')
    count=0

    for word in words:
        if len(word)<4:
            count+=1
            print(word,end=" ")
    file.close()
    print("\nThe count is",count)
display_words()
