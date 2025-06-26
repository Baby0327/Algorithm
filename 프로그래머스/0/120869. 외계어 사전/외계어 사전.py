def solution(spell, dic):
    for word in dic:
        check = True
        
        for s in spell:
            if word.count(s) != 1:
                check = False
                break
        
        if check:
            return 1
        
    return 2