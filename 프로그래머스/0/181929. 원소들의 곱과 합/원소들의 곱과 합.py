def solution(num_list):
    answer = 0
    add, mul = 0, 1
    # 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 
    for i in range(len(num_list)):
        add += num_list[i]
        mul *= num_list[i]
    if add*add > mul:
        answer = 1
    else:
        answer = 0
    return answer