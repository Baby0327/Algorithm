def solution(n):
    num = [True] * (n+1)
    num[0], num[1] = False, False
    for i in range(2, n+1):
        if num[i]:
            for j in range(i+i, n+1, +i):
                num[j] = False
    answer = n - num.count(True) - 1
    return answer