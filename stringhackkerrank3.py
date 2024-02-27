def count_substring(string, sub_string):
    length=len(string)
    lengthsub=len(sub_string)
    count=0
    if length>=1 and length<=200 :
        for i in range(length):
            if string[i:lengthsub]==sub_string :
               count+=1
            lengthsub+=1
    return count  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)