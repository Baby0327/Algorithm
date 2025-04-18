def solution(myString, pat):
    return len([1 for i in range(len(myString) - len(pat) + 1) if myString[i:i + len(pat)] == pat])