def solution(k, tangerine):
    count = {}
    
    for i in tangerine:
        count[i] = count.get(i, 0) + 1
    
    types = sorted(list(count.items()), key=lambda x : -x[1])
    total = 0
    result = 0
    
    for t, c in types:
        total += c
        result += 1
        if total >= k:
            return result
    
    return 0
    