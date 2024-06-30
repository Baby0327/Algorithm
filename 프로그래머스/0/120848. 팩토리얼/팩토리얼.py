def solution(n):
    answer = 1
    test = 1
    while test <= n:
        answer += 1
        test *= answer
    answer -= 1
    return answer