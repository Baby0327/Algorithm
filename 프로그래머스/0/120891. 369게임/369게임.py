def solution(order):
    answer = sum(str(order).count(i) for i in ["3", "6", "9"])
    return answer