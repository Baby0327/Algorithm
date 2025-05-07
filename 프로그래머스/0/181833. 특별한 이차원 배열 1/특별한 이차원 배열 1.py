def solution(n):
    answer = []
    
    for i in range(n):
        line = [0] * n
        line[i] = 1
        answer.append(line)
    
    return answer