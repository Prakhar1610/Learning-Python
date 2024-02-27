def swap_case(s):
    length=len(s)
    snew=""
    if (length>0) and (length<=1000):
        for i in range(length):
            ch=s[i]
            if (ch>='A') and (ch<='Z'):
                l=ch.lower()
                snew=snew+l
            else:
                u=ch.upper()
                snew=snew+u
        return snew
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)