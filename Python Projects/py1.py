import re
name = input("Enter deeva ko adjective: ");
match = re.search(r'ramro',name) 
match1 = re.search(r'naramro',name)
if(match1):
    print("Deeva "+name+" xa")
elif(match):
    print("Statement false")
else:
    print("Deeva "+name+" xa")