def solution(ineq, eq, n, m):
    answer = 0
    if n < m and ineq == '<' and eq == '!':
        answer = 1
    elif n > m and ineq == '>' and eq == '!':
        answer = 1
    elif n <= m and ineq == '<' and eq == '=':
        answer = 1
    elif n >= m and ineq == '>' and eq == '=':
        answer = 1
    else:
        answer = 0
    return answer