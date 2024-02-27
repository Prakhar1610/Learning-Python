r , c = map(int , input().split())
matrix = []
lst = []
for i in range(r):
    for j in range(c):
        lst.append(int(input()))
    matrix.append(lst)
    lst = []
print(matrix)