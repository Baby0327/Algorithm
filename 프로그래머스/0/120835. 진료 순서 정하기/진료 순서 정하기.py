def solution(emergency):
    n = len(emergency)
    srt = sorted([[emergency[i], i] for i in range(n)], reverse = True)
    answer = [0 for _ in range(n)]
    
    for i in range(n):
        answer[srt[i][1]] = i + 1
    
    return answer