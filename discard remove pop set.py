n = int(input())
s = set(map(int, input().split()))
operations = int(input())
for i in range(operations) :
    command = input().split()
    if command[0] == "discard" :
        s.discard(int(command[1]))
    elif command[0] == "remove" :
        s.remove(int(command[1]))
    else:
        s.pop()
print(sum(s))