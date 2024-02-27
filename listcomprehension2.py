if __name__ == '__main__':
    w = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    xyz=[]
    lst=[]
    for i in range(w+1):
        for j in range(x+1):
           for k in range(y+1):
                for l in range(z+1):
                    if (i+j+k+l) != n:
                     xyz=[i,j,k,l]
                     lst.append(xyz)
print(lst)