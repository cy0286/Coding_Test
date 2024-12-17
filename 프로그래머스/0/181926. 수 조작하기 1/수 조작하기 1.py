def solution(n, control):
    answer = 0
    
    for i in range(len(control)):
        if control[i] == 'w':
            answer = n + 1
            n = answer
        elif control[i] == 's':
            answer = n - 1
            n = answer
        elif control[i] == 'd':
            answer = n + 10
            n = answer
        else:
            answer = n - 10
            n = answer
    return answer