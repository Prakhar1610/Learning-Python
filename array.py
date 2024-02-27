arr={
     "key 1":"value 1",
     "key 2":"value 2",
    }
arr["key1"]="new value"
print(arr)

arr2=arr
arr2["new key"]="val"
print(arr)
print(arr2)
arr.clear()
print(arr)
print(arr.clear())