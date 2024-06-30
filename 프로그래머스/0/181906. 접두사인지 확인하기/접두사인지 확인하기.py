def solution(my_string, is_prefix):
    answer = int( my_string[:len(is_prefix)] == is_prefix)
    return answer