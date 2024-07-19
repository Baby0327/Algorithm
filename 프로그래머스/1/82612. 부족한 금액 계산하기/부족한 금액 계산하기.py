def solution(price, money, count):
    total = count * (2 * price + (count - 1) * price) // 2
    return total - money if total > money else 0