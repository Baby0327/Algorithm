def solution(arr):
    answer = [i[:] for i in arr]
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
                answer[i] += [0] * (len(arr) - len(arr[0]))
    elif len(arr) < len(arr[0]):
        for j in range(len(arr[0]) - len(arr)):
            answer.append([0] * len(arr[0]))
    return answer