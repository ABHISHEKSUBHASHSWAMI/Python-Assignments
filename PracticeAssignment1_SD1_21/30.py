#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#30 Program to convert USD to INR in python.

def conversion():
    opt=int(input("Enter valid option :"))
    if opt==1:
        USD=float(input("Enter Dollar amount :"))
        INR=USD*75.12
        print(USD,"$ =","Rs.",round(INR,2))
    elif opt==2:
        INR=float(input("Enter Rupees amount :"))
        USD=INR/75.12
        print("Rs.",INR,"=",round(USD,2),"$")

    else:
        print("Incorrect option!")
        conversion()

print("Choose Conversion :\n1.USD to INR\n2.INR to USD")
conversion()