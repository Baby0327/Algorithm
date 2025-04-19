def solution(date1, date2):
    day1 = sum(date1[i] * j for i, j in zip([0, 1, 2], [365, 30, 1]))
    day2 = sum(date2[i] * j for i, j in zip([0, 1, 2], [365, 30, 1]))
    
    return int(day1 < day2)