import re
string = input("Enter the string -"+"\n")
sub_string = input("Enter the string to be search -"+"\n")
l = len(sub_string)
lst = []
s1 = string.lower()

for i in range(len(string)) :
    if s1[i : l] == sub_string :
        s = re.compile(sub_string)
        p = s.findall(s1)
        lst.append(p)

final_lst = []
for j in range(len(lst)) :
    s = lst[j]
    final_lst.append(s)

print(final_lst[0])
    
    



