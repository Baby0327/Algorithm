def solution(arr):
    r = len(arr)
    c = len(arr[0])
    
    if r < c:
        for _ in range(c - r):
            arr.append([0] * c)
    elif r > c:
        for i in range(r):
            arr[i] = arr[i] + [0] * (r - c)
        
    return arr