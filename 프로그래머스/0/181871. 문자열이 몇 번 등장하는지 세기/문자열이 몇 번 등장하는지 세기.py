def solution(myString, pat):
    answer = sum([1 for i in range(len(myString) - len(pat) + 1) if myString[i:i+len(pat)] == pat])
    return answer