n = int(input())
if n>=2 and n<=10 :
    arr = map(int, input().split())
    # removing duplicate items
    arr2=list(set(arr))
    arr2.sort(reverse=True)
    print(arr2[1])


