def solution(arr):
    answer = arr[arr.index(2) : len(arr) - arr[::-1].index(2)] if arr.count(2) >= 1 else [-1]
    return answer