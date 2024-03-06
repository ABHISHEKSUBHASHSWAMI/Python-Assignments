#Name: Abhishek Subhash Swami Roll No. 4
'''. A text file named "matter.txt" contains some text, which needs to be displayed 
such that every next character is separated by a symbol "#". Write a function 
definition for hash_display() in Python that would display the entire content of the 
file matter.txt in the desired format'''

def hash_display():
    file=open('story.txt','r')
    data=file.read()
    characters=[]
    for letter in data:
        if letter.isalpha():
            characters.append(letter+"#")
    print(" ".join(characters))
    file.close()
hash_display()