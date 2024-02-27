#STRING - It stores alphabetical data by using inverted commas("abc") 
s='Hello to you.\n You like to travel'                                                 
print(s)
a='You like to travel'
print(a[0]) 
#slicing([start:stop:step]) 
print(a[2:7:3])
print(a, end='.') #end(it is used for adding any value in last of data) 
print(type(a))


#INTEGER - It stores only numeric values(123). 
a=3
b=7
c=a+b #addition 
print(c) 
print(type(c))
print(a,b,sep="k")	# sep is used as seperating data.


#COMPLEX NUMBER
a=complex(4+5j) 
print(a.real,a.imag) 
a=int(input('enter real part- ')) 
b=int(input('enter imaginary part- ')) 
c=complex(a,b) 
print(c) 
print(type(c))


#LIST - IT stores data in regular ways as list. 
a=[1,2,3]
b=[4,5,6]
print(a) 
print(a[1]) 
print(type(a)) 
a.insert(2,5) 
print(a) 
a.extend(b) 
print(a) 
a.append(7) 
c=a 
c.append(1) 
print(a) 
print(c) 
a.clear() 
print(a)


#DICTIONARY - It stores datas in forms of key and their value 
employs={
           'name':'Shyam',
           'id':'1234'
        }
print(employs.keys()) 
print(employs['id']) 
print(type(employs)) 
employs['name']='Ritesh'#UPDATING 
print(employs)
 
employs.clear() 
print(employs) 
print(employs.clear()) 
employs2=employs.copy() 
print(employs2) 
employs1=employs
print( employs1)


#tupple - Tuples are used to store multiple items in a single variable. 
a=(1,2,3)
print(a)
print(type(a))


#sets -A Set is an unordered collection data # type that is iterable, mutable and
# has no duplicate elements.
a={1,3,5}
print(a)
print(type(a))
