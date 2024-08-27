def solution(spell, dic):
    for i in dic:
        count = []
        
        for j in spell:
            count.append(i.count(j))
        
        if len(count) == count.count(1):
            return 1
    
    return 2