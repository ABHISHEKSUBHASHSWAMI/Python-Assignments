#Abhishek Subhash Swami Roll no. 4
#Create Student database using nested dictionary and remove duplicate entries of students 

database={
'Student1':{'Abhishek': 178},
'Student2':{'Arya': 155},
'Student3':{'Atharv':172},
'Student4':{'Vikas':168},
'Student5':{'Arya':155}}
newdatabase={}
for key, value in database.items():
    if value not in newdatabase.values():
        newdatabase[key]=value
print(newdatabase)