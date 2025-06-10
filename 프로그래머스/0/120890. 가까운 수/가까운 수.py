def solution(array, n):
    return sorted([[i - n, i] for i in array], key=lambda x : (abs(x[0]), x[0]))[0][1]