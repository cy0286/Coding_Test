def solution(a, b):
    answer = 0
    integer = int(str(a) + str(b))
    mul = 2 * a * b
    if integer > mul:
        answer = integer
    elif integer < mul:
        answer = mul
    else:
        answer = integer
    return answer