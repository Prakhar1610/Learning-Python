s = (input().split()).strip()

for i in s :
    if i == 0 :
        print(s[i])
    else :
        if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') and (s[i+1] == ' ') :
            print(s[i])