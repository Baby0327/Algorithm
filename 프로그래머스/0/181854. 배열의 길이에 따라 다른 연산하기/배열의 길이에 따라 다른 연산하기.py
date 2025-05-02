def solution(arr, n):
    return [arr[i] + (0 if i % 2 else n) for i in range(len(arr))] if len(arr) % 2 else [arr[i] + (0 if i % 2 == 0 else n) for i in range(len(arr))]