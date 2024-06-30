def solution(angle):
    if angle <= 90:
        answer = 1 + int(angle == 90)
    else:
        answer = 3 + int(angle == 180)
    return answer