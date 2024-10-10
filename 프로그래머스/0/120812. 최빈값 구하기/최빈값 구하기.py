def solution(array):
    dic = {}
    
    for i in array:
        dic[i] = dic.get(i, 0) + 1
    
    order = sorted(list(dic.items()), key=lambda x : -x[1])
    print(order)
    
    return -1 if len(order) > 1 and order[0][1] == order[1][1] else order[0][0]