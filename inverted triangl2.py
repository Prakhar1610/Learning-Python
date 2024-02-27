n = int(input("Enter the number- "))
for i in range(n , 0 , -1):
    for k in range(n-i+1):
        print(" ",end="")
    for j in range(i):
        print("*" , end = " ")
    print("\n")