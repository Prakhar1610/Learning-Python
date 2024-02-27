members_in_family = int(input())
rooms_list = list(map(int , input().split()))
s1 = set()
s2 = set()

if members_in_family>1 and members_in_family<1000 :
    for i in rooms_list :
       if i not in s1 :
        s1.add(i)
        s2.add(i)
       else :
        s2.discard(i)
    captain_room = list(s2)
    print(captain_room[0])   