def solution(s):
    tmp = s.split()[::-1]
    i = 0
    answer = 0
    while i < len(tmp):
        if tmp[i] != "Z":
            answer += int(tmp[i])
        else:
            i += 1
        i += 1    
    return answer