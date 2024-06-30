def solution(array):
    answer = sum(str(i).count('7') for i in array)
    return answer