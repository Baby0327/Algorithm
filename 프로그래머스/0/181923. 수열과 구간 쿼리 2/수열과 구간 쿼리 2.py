def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = sorted([i for i in arr[s:e+1] if i > k])
        answer.append(-1 if len(tmp) == 0 else tmp[0])
    return answer