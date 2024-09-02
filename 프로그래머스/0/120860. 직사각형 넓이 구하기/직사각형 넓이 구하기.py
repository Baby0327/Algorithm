def solution(dots):
    dots.sort()
    max_x, max_y = dots[-1]
    min_x, min_y = dots[0]
    answer = (max_x - min_x) * (max_y - min_y)
    
    return answer