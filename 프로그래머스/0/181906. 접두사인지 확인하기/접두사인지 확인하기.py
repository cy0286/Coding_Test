def solution(my_string, is_prefix):
    answer = 0
    word = ""
    for i in range(len(my_string)):
        word += my_string[i]
    
        if word == is_prefix and is_prefix in my_string:
            answer = 1
            return answer
        else:
            answer = 0
    return answer