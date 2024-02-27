n = int(input("Enter the number- "))
ascii1 = 97
ascii2 = 97 + n
for i in range(n):
    for k in range(n-i-1):
        print("-",end="")
    for j in range(i+1):
        alpha = chr(ascii2)
        print(alpha , end = " ")
        ascii2 = ascii2 - 1
        if ascii2 == ascii1 :
            ascii2 = ascii2 + 1
            alpha = chr(ascii2)
            print(alpha , end = " ")

    print("\n")

for i in range(n-1 , 0 , -1):
    for k in range(n-i):
        print("-",end="")
    for j in range(i):
        print("*" , end = " ")
    print("\n")
