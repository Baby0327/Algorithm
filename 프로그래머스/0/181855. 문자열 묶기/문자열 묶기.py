def solution(strArr):
    test = [0] * 31
    for i in strArr:
        test[len(i)] += 1
    answer = max(test)
    return answer