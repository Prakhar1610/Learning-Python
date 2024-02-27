if __name__ == '__main__':

    n=int(input())
    name_score=[]
    student_name=[]
    student_score=[]

    if n>=2 and n<=5 :
        for i in range(n):
            name = input()
            score = float(input())
            student_name.append(name)
            student_score.append(score)
            detail = [student_name[i] , student_score[i]]
            name_score.append(detail)
    
    student_score2 = list(set(student_score))
    student_score2.sort()
    second_low = []
    
    for j in range(len(name_score)) :
        if student_score2[1] == name_score[j][1] :
            second_low.append(name_score[j][0])
    
    second_low.sort()

    for k in range(len(second_low)) :
        print(second_low[k])