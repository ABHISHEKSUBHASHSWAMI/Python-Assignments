#Name : Abhishek Subhash Swami Roll No. 21 AI-ML
#31 Program to convert km/hr to m/s in python.

def conversion():
    opt=int(input("Enter valid option :"))
    if opt==1:
        kmph=float(input("Enter speed:"))
        m_s=kmph/3.6
        print(kmph,"km/hr =",round(m_s,2),"m/s")
    elif opt==2:
        m_s=float(input("Enter speed :"))
        kmph=m_s*3.6
        print(m_s,"m/s=",round(kmph,2),"km/hr")

    else:
        print("Incorrect option!")
        conversion()

print("Choose Conversion :\n1.km/hr to m/s\n2.m/s to km/hr")
conversion()