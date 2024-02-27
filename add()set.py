s = set()

N = int(input())

if N>0 and N<1000 :
    for i in range(N) :
        country = input()
        s.add(country)
    
print(len(s))