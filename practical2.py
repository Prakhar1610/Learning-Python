n=int(input("Enter the number- "))
c=1
for i in range(n+1):
    for j in range(i):
        if i>0 :
            print(c,end=" ")
            c=c+1  
    print("\n")
        
# using while loop        
n=int(input("Enter the number- "))
k=1
d=1
while k<=n :
    for l in range(k):      
        print(d,end=" ")
        d=d+1
    print("\n")
    k=k+1


