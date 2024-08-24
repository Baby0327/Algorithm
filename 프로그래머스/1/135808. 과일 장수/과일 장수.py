def solution(k, m, score):
    score.sort(reverse=True)
    total = 0
    
    for i in range(0, len(score)-m+1, m):
        total += min(score[i:i+m]) * m
    
    return total