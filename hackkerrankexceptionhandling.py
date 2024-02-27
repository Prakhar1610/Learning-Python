x = int(input())
for i in range(x):
    try :
        a,b = input().split()
        c = int(a)//int(b)
        print(c)
    
    except ZeroDivisionError as e :
        print("Error Code: ",e)
    
    except ValueError as v :
        print("Error Code: ",v)

    
    