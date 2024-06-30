def solution(age):
    answer = "".join(chr(int(i) + 97) for i in str(age))
    return answer