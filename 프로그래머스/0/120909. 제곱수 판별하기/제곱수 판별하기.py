import math

def solution(n):
    answer = 0
    
    if int(math.sqrt(n)) == math.sqrt(n):
        answer = 1
    else:
        answer = 2
    return answer