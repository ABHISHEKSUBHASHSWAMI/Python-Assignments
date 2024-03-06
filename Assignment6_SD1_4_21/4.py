#Generate a Python list of all the even numbers between 4 to 30

def gen(a,b):
    ls=[]
    for i in range(a,b+1):
        if(i%2==0):
            ls.append(i)
    return ls
print(gen(4,30))