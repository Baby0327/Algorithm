def solution(order):
    latte = len([1 for i in order if "latte" in i])
    
    return 5000 * latte + 4500 * (len(order) - latte)