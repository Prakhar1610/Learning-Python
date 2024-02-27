EN = int(input())
ren = set(map(int , input().split()))

FN = int(input())
rfn = set(map(int , input().split()))

if EN>0 and EN<1000 and FN>0 and FN<1000 :
    s = ren.union(rfn)
    print(len(s))