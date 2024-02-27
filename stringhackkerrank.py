def split_and_join(line):
    for i in range(len(line)):
        if line[i]==" " :
            new_line=line.replace(" ","-")
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#another way
def split_and_join(line):
    new_line=line.replace(" ","-")
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)