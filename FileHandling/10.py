#Name: Abhishek Subhash Swami Roll No: 4
'''Aditi has used a text editing software to type some text. After saving the article 
as WORDS.TXT, she realised that she has wrongly typed alphabet J in place of 
alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the corrected 
version of entire content of the file WORDS.TXT with all the alphabets "J" to be 
displayed as an alphabet "I" on screen'''

def JTOI():
    file=open('words.txt','r')
    data=file.read()
    for letter in data:
        if letter=='J':
            print('I',end='')
        else:
            print(letter,end='')
    file.close()
JTOI()