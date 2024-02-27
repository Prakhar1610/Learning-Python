import modularity1 as m1

x = int(input())
y = int(input())

answer_1 = []
answer_2 = []
answer_3 = []
answer_4 = []
answer_5 = []

answer_1.append(m1.add(x , y))
answer_2.append(m1.sub(x , y))
answer_3.append(m1.mult(x , y))
answer_4.append(m1.div(x , y))
answer_5.append(m1.mod(x , y))

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)
print(answer_5)