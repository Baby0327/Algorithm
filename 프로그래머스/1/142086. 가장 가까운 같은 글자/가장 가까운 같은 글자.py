def solution(s):
    answer = []
    
    for i in range(len(s)):
        answer.append(-1)
        for j in range(i):
            if s[i] == s[j]:
                answer[-1] = i - j
                
    return answer