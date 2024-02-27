dict1={
        "Name":"Prakhar Singh",
        "Section":"CCML",
        "DOB":"16/10/2003"
       }
k=input("Enter the key-"+"\n")
for k in dict1.keys():
    if k in dict1:
        print(dict1[k])
        break
    else:
        v=input("Enter the value-"+"\n")
        dict1.insert(dict1[])       

#k=input("Please input a key: ") 
#v=input("Plesse input a value: ") 
#classe_list={k:v} 
#print(classe_list)