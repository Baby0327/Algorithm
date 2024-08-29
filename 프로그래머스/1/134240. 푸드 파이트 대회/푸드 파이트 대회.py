def solution(food):
    answer = '0'
    
    for i in range(len(food)-1, 0, -1):
        dish = str(i) * (food[i] // 2)
        answer = dish + answer + dish
        
    return answer