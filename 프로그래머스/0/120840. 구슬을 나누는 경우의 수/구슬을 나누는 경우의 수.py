def solution(balls, share):
    top = 1
    bottom = 1
    for i in range(balls, balls - share, -1):
        top *= i
    for i in range(share, 0, -1):
        bottom *= i
    answer = top // bottom
    return answer