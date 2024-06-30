def solution(n):
    answer = [n]
    while answer[-1] != 1:
        answer.append(answer[-1] // 2 if answer[-1] % 2 == 0 else answer[-1] * 3 + 1)
    return answer