def solution(num_list):
    answer = []
    num_list.sort()
    # list comprehension
    answer = [num_list[i] for i in range(5, len(num_list))]
    return answer