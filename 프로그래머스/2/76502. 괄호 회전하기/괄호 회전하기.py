def solution(s):
    answer = 0
    dic = {"[" : "]", "(" : ")", "{" : "}"}
    
    for i in range(len(s)):
        now = s[i:] + s[:i]
        temp = []
        for j in now:
            if temp and temp[-1] in dic and dic[temp[-1]] == j:
                temp.pop()
            else:
                temp.append(j)
        if not temp:
            answer += 1
        
    return answer