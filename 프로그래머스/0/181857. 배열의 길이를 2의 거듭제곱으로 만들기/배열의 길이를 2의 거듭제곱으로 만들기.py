def solution(arr):
    if len(arr) == 1:
        answer = arr
    else:
        i = 0
        while True:
            if len(arr) > 2**i and len(arr) <= 2**(i+1):
                break
            i += 1
        answer = arr + [0] * (2**(i+1) - len(arr))
    return answer