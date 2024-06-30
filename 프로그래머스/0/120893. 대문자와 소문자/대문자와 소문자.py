def solution(my_string):
    answer = "".join(i.upper() if i.islower() else i.lower() for i in my_string)
    return answer