#Program to calculate compound interest

principle=int(input("Enter principle :"))
rate=int(input("Enter rate of interest in % :"))
time=int(input("Enter the time period in yr :"))

cmpndintrst=principle*(1+rate/100)**time

print("Compound Interest for",time,"years is",int(cmpndintrst))