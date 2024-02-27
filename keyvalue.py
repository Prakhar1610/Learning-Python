dict1={
       "Name":"Prakhar Singh",
       "Section":"CCML",
       "DOB":"16/10/2003"
     }
 
k=input("Enter the key-"+"\n")

if k in dict1:
    print(dict1[k])

else:
    v=input("Enter the value-"+"\n")
    dict2={
            k:v                                     # making another dictionary
          }
    combine={**dict1,**dict2}             # merging two dictionaries
    print("Combined dictionary is-")
    print(combine)

