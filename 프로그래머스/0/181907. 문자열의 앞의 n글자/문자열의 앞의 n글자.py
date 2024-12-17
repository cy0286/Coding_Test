def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer = answer + my_string[i]
        if i == n-1:
            return answer
    return answer