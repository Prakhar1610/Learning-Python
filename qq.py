string = input()
max_width = int(input())
for i in range(0 , len(string) , max_width) :
        ns = string[i : i+max_width]
        print(ns)
