def solution(n, k):
    answer = 0
    answer = 12000 * n + 2000 * k
    temp = n // 10
    if (n >= 10):
        answer = answer - (2000 * temp)
    return answer