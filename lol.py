M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))
mdef = mset.difference(nset)
ndef = nset.difference(mset)
output = mdef.union(ndef)
lst = list(output)
lst.sort()
for i in range(len(lst)):
    print(lst[i])
p ="asv"
p.capitalize