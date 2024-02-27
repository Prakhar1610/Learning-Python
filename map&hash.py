n=int(input())
l=map(int,input().split())
print(l)
lst=[]
for i in l:
    lst.append(i)
t=tuple(lst)
print(t)
print(hash(t))