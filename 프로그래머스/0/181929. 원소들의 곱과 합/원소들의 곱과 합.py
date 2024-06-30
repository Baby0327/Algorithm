from math import *

def solution(num_list):
    answer = int(sum(num_list)**2 > prod(num_list))
    return answer