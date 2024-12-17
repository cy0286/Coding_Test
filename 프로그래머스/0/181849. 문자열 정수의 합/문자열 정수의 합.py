def solution(num_str):
    answer = 0
    for i in range(len(str(num_str))):
                   answer += int(num_str[i])
    return answer

# def solution(num_str):
#    return sum(map(int, (num_str)))
