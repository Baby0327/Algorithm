def solution(order):
    return len([1 for i in str(order) if i in "369"])