def solution(a, b):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    return answer[(sum(day[:a]) + b) % 7]