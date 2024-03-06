#program to calculate simple interest
principle=int(input("Enter Principle :"))
rate=int(input("Enter % rate of the interest :"))
time=int(input("Enter time period in years :"))
interest=principle*rate*time/100
print("Simple Interest=",interest)
amount=principle+interest
print("Amount=",amount)