def solution(lines):
    line = [0] * 200
    
    for start, end in lines:
        for i in range(start, end):
            line[i] += 1
            
    return len([1 for i in line if i > 1])