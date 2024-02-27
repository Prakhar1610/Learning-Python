n = int(input("Enter the number- "))
for i in range(n):
    for k in range(n-i-1):
        print("1",end="")
    for j in range(i+1):
        print("*" , end = " ")
    print("\n")