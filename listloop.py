#printing each item of list using for loop
lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(lst[i])

#another way of printing each item of list using for loop
lst=[1,2,3,4,5]
for i in lst:
    j=i-1
    print(lst[j])

#printing each item of list using while loop
lst = ["apple", "banana", "mango"]
i = 0
while i < len(lst):
  print(lst[i])
  i = i + 1

#printing each item of list using short hand for loop
lst = ["apple", "banana", "mango"]
[print(x) for x in lst]

# user input list
n=int(input("Enter the number- "))
lst=[]  #empty list

for i in range(n):
    lst.append(i)  #adding items to lst
print(lst)

# user input list using for loop
lst1=[]   #empty list
lst2=[]   #empty list
for i in range(n):
    m=input("Enter items- "+"\n")
    if m.isdigit():
        m=int(m)
        lst1.append(m)
    else:
        lst1.append(m)
lst2=lst2+lst1   #combining two list
print(lst2)

# user input list using while loop
lst1=[]
lst2=[]
n=int(input("Enter number of items- "+"\n"))
i=0
while (i<n):
    m=input("Enter items- "+"\n")
    if m.isdigit():
        m=int(m)
        lst1.append(m)
    else:
        lst1.append(m)
    i=i+1        
lst2=lst2+lst1   
print(lst2)