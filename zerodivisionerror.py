try :
    a,b = input().split()
    c = int(a)//int(b)
    print(c)    
except ZeroDivisionError as e :
    print("Error Code: ",e)