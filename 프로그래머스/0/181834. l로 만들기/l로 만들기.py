def solution(myString):
    answer = ''
    for i in range(len(myString)):
        answer = answer + myString[i]
        if myString[i] < 'l':
            answer = answer.replace(myString[i], 'l')
    return answer