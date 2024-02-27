n , m = map(int , input().split())
arr = list(map(int , input().split()))
A = set(map(int , input().split()))
B = set(map(int , input().split()))

if n>=1 and n<=10**5 and m>=1 and m<=10**5 :
    happiness = 0
    l1 = list(A)
    l2 = list(B)
    
    for i in range(len(arr)) :
        if arr[i] in l1 :
            happiness = happiness+1
        else :
            happiness = happiness-1
    print(happiness)