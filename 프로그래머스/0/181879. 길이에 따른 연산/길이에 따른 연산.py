from math import *

def solution(num_list):
    answer = sum(num_list) if len(num_list) > 10 else prod(num_list)
    return answer