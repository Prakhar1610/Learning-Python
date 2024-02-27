import textwrap
def wrap(string, max_width):
    for i in range(0 , len(string) , max_width) :
        ns = string[i : i+max_width]
        if len(ns) == max_width :
            print(ns)
        else :
            return ns

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)