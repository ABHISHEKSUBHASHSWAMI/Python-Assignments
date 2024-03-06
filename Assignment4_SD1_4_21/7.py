#Abhishek Subhash Swami Roll no. 4
#WAP to check whether a given key already exists in a dictionary.

smartphones={"Samsung":"S21","Apple":"iPhone 13","Xiaomi":"Mi 11","Poco":"F3 GT"}
key=input("Enter key value to be verified :")
if key in smartphones.keys():
    print("Key is present !\nValue :",smartphones[key])
else:
    print("Provided key is not found !")