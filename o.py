lst1=[[1,2,3],
      [4,5]]
lst2=lst1.insert((lst1[1][0]),10)
#lst2=lst[1].insert(0,10)
print(lst2)

l=[[1,2,3],
   [4,[5,6]],
   [7,8,[9,10]],
   [11,12]]
print(l[1][1][1])
print(l[2][2][0])
l[2][2].insert(1,2)
print(l)

l=[[1,2,3],
   [4,[5,6]],
   [7,8,[9,10]],
   [11,12]]
l[2][2].insert(1,0)
print(l)