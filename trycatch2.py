try:
    a1=input("Enter your age- ""\n")
    a1=int(a1)
    print("Your age is: ")
    print(a1)
except TypeError:
    print("Enter valid number")