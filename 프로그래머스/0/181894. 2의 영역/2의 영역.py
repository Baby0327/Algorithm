def solution(arr):
    if 2 in arr:
        start = arr.index(2)
        end = arr[::-1].index(2)
        return arr[start:-end] if end else arr[start:]
    else:
        return [-1]