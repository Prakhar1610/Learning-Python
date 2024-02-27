a=5
b=7
print(a&b)     # & multiply
print(a|b)     # | add
a=3
b=5
print(a&b)

# <<  left
# >>  right
a=5
b=a<<1   #shifts bits by 1 towards left(multiplying a by 2 one time)
print(b)

a=5
b=a<<2    # shifts bits by 2 towards left(multiplying a by 2 two time)
print(b)

a=5
b=a<<3      # shifts bits by 3 towards left(multiplying a by 2 three time)
print(b)

a=80
b=a>>1
print(b)     # shifts bits by 1 towards right(dividing a by 2 one time)

a=80
b=a>>2
print(b)     # shifts bits by 2 towards right(dividing a by 2 two time)

a=80
b=a>>3
print(b)     # shifts bits by 3 towards right(dividing a by 2 three time)