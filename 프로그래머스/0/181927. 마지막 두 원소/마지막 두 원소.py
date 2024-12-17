def solution(num_list):
    answer = []
    if num_list[-1] > num_list[-2]:
        answer.extend(num_list)
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.extend(num_list)
        answer.append(num_list[-1] * 2)
    return answer