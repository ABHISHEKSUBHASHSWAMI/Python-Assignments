#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#41 Program to print Prime numbers within given interval

def limiter(a,b):
    primes=[]
    count=0
    if a<2:
        a=2
    for i in range(a,b+1):
        prime=1
        for j in range(2,(i//2)+1):
            if i%j==0:
                prime=0
                break
        if prime==1:
            primes.append(str(i))
            count+=1
    print("\nThere are",count,"prime numbers.")
    print(",".join(primes),"\n")

lower=int(input("Enter lower limit :"))
upper=int(input("Enter upper limit :"))

limiter(lower,upper)