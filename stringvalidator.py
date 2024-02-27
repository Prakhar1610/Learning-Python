if __name__ == '__main__':
    s = str(input())
    length = len(s)
    alnum=0
    alpha=0
    digit=0
    lower=0
    upper=0
    if length>0 and length<1000 :
       for i in range(length):
        if(alnum==0 or alpha==0 or digit==0 or lower==0 or upper==0):
            if(s[i].isalnum()):
                alnum=1
            if (s[i].isalpha()):
                alpha =1
            if (s[i].isdigit()):
                digit=1
            if (s[i].islower()):
                lower=1    
            if (s[i].isupper()):
                upper=1
    print(bool(alnum))
    print(bool(alpha))
    print(bool(digit))
    print(bool(lower))
    print(bool(upper))



# another way


            
        