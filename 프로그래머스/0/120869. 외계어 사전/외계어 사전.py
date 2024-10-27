def solution(spell, dic):
    for i in dic:
        check = []
        for j in spell:
            check.append(i.count(j))
        if len(check) == check.count(1):
            return 1
    return 2