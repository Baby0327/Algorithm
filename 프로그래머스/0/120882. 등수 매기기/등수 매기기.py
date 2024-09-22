def solution(score):
    avg = []
    
    for i, j in score:
        avg.append((i + j) / 2)
        
    answer = []
    
    for i in range(len(avg)):
        rank = 1
        for j in range(len(avg)):
            if avg[i] < avg[j]:
                rank += 1
        answer.append(rank)
    
    return answer