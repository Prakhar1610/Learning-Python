l1 = ["P" , "Q" , "R" , "S" , "T"]
l2 = [4 , 2 , 7 , 9 , 5]
l4 = []
for i in range(len(l1)) :
    l3 = [l1[i] , l2[i]]
    l4.append(l3)

print(l4)

dict = dict(l4)
   
print(dict)

min_1 = dict[0]
print(min_1)

for key in dict :
    m1 = dict[key]
    