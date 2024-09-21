def solution(A, B):
    answer = -1
    
    for i in range(len(A), 0, -1):
        if A[i:] + A[:i] == B:
            answer = len(A) - i
            break
    
    return answer