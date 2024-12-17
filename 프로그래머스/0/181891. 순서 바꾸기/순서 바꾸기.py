def solution(num_list, n):
    answer = []
    whole_list = []
    n_list = []
    for i in range(n, len(num_list)):
        whole_list.append(num_list[i])
    for i in range(n):
        n_list.append(num_list[i])
    answer = whole_list + n_list
    return answer