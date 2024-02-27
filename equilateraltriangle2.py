n = int(input("Enter the number- "))
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range((i+1)+1):
        print("*" , end = " ")
        #c = c+1
    print("\n")