def solution(num_list):
    answer = 0
    temp1 = 0
    temp2 = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            temp1 += num_list[i]
        else:
            temp2 += num_list[i] 
    if temp1 > temp2:
        answer = temp1
    elif temp1 < temp2:
        answer = temp2
    else:
        answer = temp1
    return answer