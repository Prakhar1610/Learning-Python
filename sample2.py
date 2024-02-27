# user input dictionary using for loop
n=int(input("Enter number of student- "))
d = dict()
for i in range(n):  
    k=input("Enter the student's name- ")
    v=input("Enter the roll number- ")
    d[k] = int(v)
print(d)


# user input dictionary using while loop
n=int(input("Enter number of student- "))
e = dict()
i=0
while i<n:
    k=input("Enter the student's name- ")
    v=input("Enter the roll number- ")
    e[k] = int(v)
    i=i+1
print(e)