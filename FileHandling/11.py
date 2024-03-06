#Name: Abhishek Subhash Swami Roll NO. 4
'''Write a function AMCount() in Python, which should read each character of a text 
file STORY.TXT, should count and display the occurance of alphabets A and M 
(including small cases a and m too).'''

def AMcount():
    file=open('story.txt','r')
    data=file.read()
    countA,countM=0,0
    for letter in data:
        if letter.lower()=='a':
            countA+=1
        elif letter.lower()=='m':
            countM+=1
    print("A : %d\nM : %d" %(countA,countM))
    file.close()
AMcount()