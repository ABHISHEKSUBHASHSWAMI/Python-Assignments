#Name : Abhishek Subhash Swami Roll No. 21 AI-ML

#12 Write a Python function that takes a list of words and returns the length of the longest one.

list=['Entertainment','entire','Elephant','inconsequential']
longest=0

for words in list:
    if len(words)>longest:
        longest=len(words)
        longest_word=words

print("Longest word is",longest_word, "with", len(longest_word), "letters.")