def solution(arr):
    answer = [arr[0]]
    for i in arr:
        # 연속되지 않은 수만 저장
        if answer[-1] != i:
            answer.append(i)
    return answer