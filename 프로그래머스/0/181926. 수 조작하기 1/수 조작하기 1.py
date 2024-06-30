def solution(n, control):
    char = {"w":+1, "s":-1, "d":+10, "a":-10}
    for i in control:
        n += char[i]
    answer = n
    return answer