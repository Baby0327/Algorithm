def solution(s):
    return s[len(s)//2] if len(s) % 2 == 1 else "".join(s[len(s)//2 - 1 : len(s)//2 + 1])