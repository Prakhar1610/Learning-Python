n = int(input())
nm = []
for i in range(n) :
    data = input().split()
    l = [data[0] , [data[1] , data[2] , data[3]]]
    nm.append(l)
print(nm)
d = dict(nm)
print(d)