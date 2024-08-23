def solution(k, score):
    honor = []
    answer = []
    
    for i in score:
        honor.append(i)
        honor.sort(reverse=True)
        
        if len(honor) > k:
            honor = honor[:k]
            answer.append(honor[k-1])
        else:
            answer.append(honor[-1])
        
    return answer