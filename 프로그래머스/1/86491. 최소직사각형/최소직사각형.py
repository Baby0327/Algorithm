def solution(sizes):
    mini = 0
    maxi = 0
    
    for i in sizes:
        temp = sorted(i)
        mini = max(mini, temp[0])
        maxi = max(maxi, temp[1])
    
    return mini * maxi