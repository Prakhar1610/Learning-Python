import re
string = input("Enter the string -"+"\n")
sub_string = input("Enter the string to be search -"+"\n")
re.IGNORECASE
s = re.compile(sub_string)
p = s.search(sub_string)
print(p)
