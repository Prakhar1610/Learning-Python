lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
print(lst[1][1])
print(type(lst[1]))

lst2=[1,2,3,4,5,"Prakhar"]
lst2.remove(lst2[5])
print(lst2)
lst2.remove(1)
print(lst2)
lst3=lst2.copy()         # .copy() does deep copying
lst3.append(7)           
print(lst3)
lst3.append(0)                     
print(lst3)
print(lst2)

lst4=lst2        # shallow copy
lst4.append(7)           
print(lst4)
lst4.append(0)                     
print(lst4)
print(lst2)

lst5=[1,2]
lst6=[3,4]
lst5.append(lst6)
print(lst5)
lst5.extend(lst6)
print(lst5)

l=[1,2,3,4,5]
print(l.pop())

l=[1,2,3,4,5]
print(l.sort())
l=[9,5,7,2,3]
l.sort()
print(l)
l=[5,5,6,2,3]
l.sort()
print(l)

l=[56,89,32,90,12]
l.reverse()
print(l)

l=[89,37,56,78,10]
l.sort( reverse=True)
print(l)


