import math
AB , BC = int(input()) , int(input())
AC = math.sqrt(AB**2 + BC**2)
CM = AC/2
angle = math.degrees(math.acos((BC/2)/CM))
print(str(int(round(angle)))+chr(176))