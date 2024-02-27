# n = int(input())
# arr2=[]
# if n>=2 and n<=10 :
#     arr = map(int, input().split())

# def removing_duplicate_values():
#     new_arr=list(set(arr))       
#     return new_arr

# def removing_max_value():
#     max_arr=removing_duplicate_values()
#     m=max(max_arr)
#     length=len(max_arr)
#     for i in range(length):
#         if max_arr[i] == m :
#             max_arr.pop(i)
#             arr2.append(max_arr)
#     return arr2

# def runner_up_score():
#     arr3=removing_max_value()
#     rn_up_sc=arr3[0]
#     length=len(arr3)
#     for i in range(length):
#         if arr3[i]>rn_up_sc :
#             rn_up_sc=arr3[i]
#     print(rn_up_sc)

# runner_up_score()




ls = [1,2,3,4,5,6,7,5,4,3,2,45,45,33,3]

st = set(ls)
ls = list(st)

ls.sort()
print(ls)