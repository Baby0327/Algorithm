def solution(num, total):
    middle = total // num
    return [i for i in range(middle - num // 2 + int(num % 2 == 0), middle + num // 2 + 1)]