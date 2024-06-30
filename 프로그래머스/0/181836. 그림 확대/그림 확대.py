def solution(picture, k):
    answer = []
    for i in picture:
        tmp = ""
        for j in i:
            tmp += j * k
        for j in range(k):
            answer.append(tmp)
    return answer