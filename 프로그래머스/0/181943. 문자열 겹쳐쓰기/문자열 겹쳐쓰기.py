def solution(my_string, overwrite_string, s):
    answer = ''  

    answer = my_string[:s] + overwrite_string
    for i in range(len(answer), len(my_string)):
        answer = answer + my_string[i]
    return answer