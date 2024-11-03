def solution(data, col, row_begin, row_end):
    mod = []
    data.sort(key=lambda x : (x[col - 1], -x[0]))
    
    for i in range(row_begin - 1, row_end):
        temp = 0
        for j in range(len(data[i])):
            temp += data[i][j] % (i + 1)
        mod.append(temp)
    
    answer = mod[0]

    
    for i in range(1, len(mod)):
        answer = answer ^ mod[i]
    
    return answer