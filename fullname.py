def getFirst_Name():
    first_name = input("Enter the First Name-"+"\n")
    return first_name

def getLast_Name():
    last_name = input("Enter the Last Name-"+"\n")
    return last_name

def getFull_Name():
    first=getFirst_Name()
    last=getLast_Name()
    full_name=first+" "+last
    print(full_name)

getFull_Name()

