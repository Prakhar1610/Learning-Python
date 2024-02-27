if __name__ == '__main__':

    n = int(input())
    names_marks = []

    for i in range(n):
        data = input().split()
        l = [data[0] , [float(data[1]) , float(data[2]) , float(data[3])]]
        names_marks.append(l)

    record = dict(names_marks)
    
    name = input()
    if name in record :
        marks = record[name]
        average = sum(marks)/len(marks)
        print("%.2f" % average)