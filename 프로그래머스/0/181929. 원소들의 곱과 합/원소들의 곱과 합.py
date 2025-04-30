def solution(num_list):
    m = 1
    s = sum(num_list)**2
    
    for i in num_list:
        m *= i
    
    return int(m < s)