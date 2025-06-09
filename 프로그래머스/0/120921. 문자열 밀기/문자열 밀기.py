def solution(A, B):
    l = len(A)
    
    for i in range(l):
        if A[-i:] + A[:-i] == B:
            return i
    
    return -1