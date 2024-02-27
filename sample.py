abc={
     "k1":[1,2,3,4,5],
     "k2":[6,7,8,9,{1:"hello",2:"Bye"}]
}
print(abc)
print(abc["k2"][4][2])
print(abc["k1"][3])
print(type(abc["k2"][4]))
print(type(abc["k2"][4][1]))
print(abc["k2"][4][1][0])
print(abc["k2"][4][1].isdigit())

d=[1,2,3,{"k1":[1,2,3,4,5],
          "k2":"String"}]
print(d[3]["k1"])
print(d[3]["k2"])
print(d[3]["k1"][4])
print(d[3]["k2"][3])
