# list-index based array

lst=[1,2,3]
print(lst)
lst.remove(1)
print(lst)

lst1=[1,2,3,"4"]
print(lst1)

lst2=[1,2,3,"4","Prakhar",3+9j]
print(lst2)
print(lst2[1])
print(lst[0])
print(type(lst2[0]))
print(type(lst2[5]))

l=[1,2,3,4]
l.remove(l[0])
print(l)

#age="10"
#if age.isdigit():
 #print("Age is in number")                      

#age1="10"
#if age1.isnumeric():
 #print("Age is in number") 

#age2="अ"
#if age2.isnumeric():
 #print("Age is in number") 

age3="集中"
if age3.isnumeric():
 print("Age is in number") 
else:
    print("Not a digit")