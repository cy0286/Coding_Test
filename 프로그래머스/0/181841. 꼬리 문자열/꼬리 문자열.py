def solution(str_list, ex):
    answer = ''
    answer2 = ''
    for i in range(len(str_list)):
        answer += str_list[i]
        for j in range(len(str_list[i])):
            if ex in str_list[i]:
                answer2 = str_list[i]
            if answer2 in answer:
                answer = answer.replace(answer2, "")
    return answer