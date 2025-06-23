def solution(picture, k):
    answer = []
    
    for line in picture:
        answer += ["".join([i*k for i in line])] * k
            
    return answer