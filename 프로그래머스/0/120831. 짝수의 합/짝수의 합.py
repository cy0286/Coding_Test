def solution(n):
    answer = 0
    temp = []
    
    for i in range(1, n + 1):
        if (i % 2 == 0):
            temp.append(i)
    answer = sum(temp)
    return answer