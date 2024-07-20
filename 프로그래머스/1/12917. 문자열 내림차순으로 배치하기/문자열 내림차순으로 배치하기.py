def solution(s):
    upper = ""
    lower = ""
    
    for i in s:
        if i.isupper():
            upper += i
        else:
            lower += i
            
    answer = "".join(sorted(lower, reverse = True)) + "".join(sorted(upper, reverse = True))
    
    return answer