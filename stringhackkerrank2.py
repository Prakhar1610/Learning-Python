def mutate_string(string, position, character):
    l=list(s)
    l[position]=character
    new_s=""
    for i in range(len(l)):
        if i==position :
            l[i]=character
            new_s=new_s+l[i]
        else:
            new_s=new_s+l[i]
    return new_s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# another way
def mutate_string(string, position, character):
    l=list(s)
    l[position]=character
    new_s="".join(l)
    return new_s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)    