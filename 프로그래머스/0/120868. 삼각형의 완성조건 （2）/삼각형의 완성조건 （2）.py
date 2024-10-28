def solution(sides):
    answer = sum(1 for _ in range(max(sides) - min(sides) + 1, max(sides) + 1)) + sum(1 for _ in range(max(sides) + 1, sum(sides)))
    return answer