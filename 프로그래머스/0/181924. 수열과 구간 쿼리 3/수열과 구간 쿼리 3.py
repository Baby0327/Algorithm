def solution(arr, queries):
    answer = arr[:]
    for s, e in queries:
        answer[s], answer[e] = answer[e], answer[s]
    return answer