# Simple method of using ternary operator
a,b=10,20
m=a if a<b else b
print(m)

# Direct method by using tuples,dictionary,lambda
a,b=10,20

# 1-
print((b,a) [a<b])

# 2-
print({True : a, False : b} [a<b])

# 3-
print((lambda : b, lambda : a) [a<b])

