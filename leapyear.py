#is_leap() when parameterized with year
def is_leap(year):
    if (year>=1900) and (year<=10**5) :
        if (year%400==0) or ((year%4==0) and (year%100!=0)):
            return True
        else:
            return False
    else: 
        print("Wrong input") 
year=int(input("Enter the year- "))  
print(is_leap(year))

#is_leap() when non parameterized
def is_leap():
    year=int(input("Enter the year- ")) 
    if (year>=1900) and (year<=10**5) :
        if (year%400==0) or ((year%4==0) and (year%100!=0)):
            return True
        else:
            return False
    else: 
        print("Wrong input")  
print(is_leap())