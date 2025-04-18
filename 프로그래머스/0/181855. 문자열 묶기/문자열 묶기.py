def solution(strArr):
    cnt = {}
    
    for i in strArr:
        cnt[len(i)] = cnt.get(len(i), 0) + 1
        
    return sorted(cnt.items(), key=lambda x : x[1])[-1][1]