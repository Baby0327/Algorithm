def solution(lines):
    count = {}
    
    for s, e in lines:
        for i in range(s, e):
            count[i] = count.get(i, 0) + 1
    
    return len(sorted(filter(lambda x : x[1] > 1, count.items())))