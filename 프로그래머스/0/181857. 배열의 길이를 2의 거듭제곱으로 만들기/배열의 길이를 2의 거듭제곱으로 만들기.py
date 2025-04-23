def solution(arr):
    while len(arr) & len(arr) - 1:
        arr.append(0)
    
    return arr