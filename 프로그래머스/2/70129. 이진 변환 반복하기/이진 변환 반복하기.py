def solution(s):
    count = 0
    zero = 0

    while s != "1":
        now = s.replace("0", "")
        zero += len(s) - len(now)
        s = bin(len(now))[2:]
        count += 1

    return [count, zero]