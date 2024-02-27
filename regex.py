import re
string = "8264992734"
pattern = re.compile("\d")
print(pattern)
print(pattern.findall(string))

string = "8264992734 123456"
pattern = re.compile("\d")
print(pattern.findall(string))

string = "8264992734 g 123456"
pattern = re.compile("\D")
print(pattern.findall(string))

string = "8264992734 g 123456"
pattern = re.compile("\w")
print(pattern.findall(string))

string = "8264992734 g 123456"
pattern = re.compile("\W")
print(pattern.findall(string))

string = "8264992734 g 123456"
pattern = re.compile("\s")
print(pattern.findall(string))

string = "8264992734 g. 123456"
pattern = re.compile("\.")
print(pattern.findall(string))

string = "8264992734 g 123456"
pattern = re.compile("\.")
print(pattern.findall(string))

string = "8264992734+g+123456"
pattern = re.compile("\+")
print(pattern.findall(string))

string = "8264992734+Prakhar+123456"
pattern = re.compile("Prakhar")
print(pattern.findall(string))

string = "  8264992734      123456"
pattern = re.compile("\d")
print(pattern.search(string))

string = "8264992734123456"
pattern = re.compile("\d")
print(pattern.search(string))

string = "8264992734+Prakhar+123456 Prakhar"
pattern = re.compile("Prakhar")
print(pattern.findall(string))