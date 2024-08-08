def prime(n):
    num = [True] * (n+1)
    num[0], num[1] = False, False
    
    for i in range(2, int(n**0.5) + 1):
        if num[i]:
            for j in range(i*2, n+1, i):
                num[j] = False
    
    return num

def solution(n):
    num = prime(n)
    answer = 0
    
    for i in range(n+1):
        if num[i]:
            answer += 1
        
    return answer