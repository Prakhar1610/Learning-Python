detail={
        "name":"Prakhar",
        "class":"Btech",
        "roll no":"1210438045",
        "phone number":"8264992734"
       }
print(detail) 
print(detail["name"])

nv=detail.keys()
keys = list(nv)
key = keys[1]
print(key)

print(detail.get("class"))

if "name" in detail.keys():
    print("Exists")
else:
    print("Not Exists")

val=detail.values()
print(val)
